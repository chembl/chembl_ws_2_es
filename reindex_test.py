import os
import sys
import requests
import copy
from concurrent.futures import ThreadPoolExecutor, Future
import json
import time
import signal
import traceback
from threading import Lock

SCRIPT_PATH = os.path.realpath(__file__)
SCRIPT_DIR = os.path.abspath(os.path.join(SCRIPT_PATH, os.pardir))
GLADOS_ES_PATH = os.path.join(SCRIPT_DIR, 'src')
sys.path.append(GLADOS_ES_PATH)

from glados.es.ws2es.progress_bar_handler import get_new_progressbar

base_url = 'http://hx-rke-wp-webadmin-04-worker-4.caas.ebi.ac.uk:32000'
task_ids = []
sync_lock = Lock()
es_auth = ('elastic', '')
stop_reindex = False


def termination_handler(stop_signal, frame):
    global sync_lock, es_auth, stop_reindex
    stop_reindex = True
    print('STOPPING PRE-LOCK', file=sys.stderr)
    sys.stderr.flush()
    sync_lock.acquire()
    print('STOPPING POST-LOCK', file=sys.stderr)
    sys.stderr.flush()
    try:
        for task_id_i in task_ids:
            cancel_req = requests.post(url=base_url+'/_tasks/{0}/_cancel'.format(task_id_i), auth=es_auth)
            print('CANCEL REQ ANS: {0}'.format(cancel_req.json()), file=sys.stderr)
    except:
        traceback.print_exc(file=sys.stderr)
    sys.stderr.flush()
    sync_lock.release()


signal.signal(signal.SIGTERM, termination_handler)
signal.signal(signal.SIGINT, termination_handler)


base_request_path = '/_reindex?wait_for_completion=false&refresh=false&wait_for_active_shards=all'

base_reindex_data = {
    'source': {
        'index': 'unichem_bkp_simple',
        'size': 500,
        'slice': {
            'id': 2,
            'max': 1000
        }
    },
    'dest': {
        'index': 'unichem_sss_{0}'
    }
}

num_slices = 1000
initial_time = time.time()
sleep_time = 10
pb_scheduled = get_new_progressbar('scheduled_slices', max_val=num_slices)
pb_reindexed = get_new_progressbar('reindex_slices', max_val=num_slices)
scheduled_slices = 0
completed_slices = 0
slice_reindex_timeout = sleep_time * 1000


def reindex_slice(slice_index):
    global completed_slices, scheduled_slices, task_ids, sleep_time, pb_scheduled, pb_reindexed, slice_reindex_timeout,\
        base_url, base_request_path, base_reindex_data, sync_lock, es_auth, stop_reindex
    if stop_reindex:
        return

    dest_index = slice_index % 10
    task_id = None
    sync_lock.acquire()
    try:
        cur_reindex_data = copy.deepcopy(base_reindex_data)
        cur_reindex_data['source']['slice']['id'] = slice_index
        cur_reindex_data['dest']['index']= cur_reindex_data['dest']['index'].format(dest_index)
        start_req = requests.post(
            url=base_url+base_request_path,
            auth=es_auth,
            json=cur_reindex_data
        )
        task_id = start_req.json()['task']
        task_ids.append(task_id)
        scheduled_slices += 1
        pb_scheduled.update(scheduled_slices)
        print('START REQ {0}: {1}'.format(slice_index, json.dumps(cur_reindex_data)), file=sys.stderr)
        print('START REQ ANS: {0}'.format(start_req.json()), file=sys.stderr)
        sys.stderr.flush()
    except:
        traceback.print_exc(file=sys.stderr)
    sync_lock.release()

    if task_id is None:
        return

    completed = False
    req_start_time = time.time()
    while not completed and not stop_reindex:
        time.sleep(sleep_time)
        status_req = requests.get(
            url=base_url+'/_tasks/{0}'.format(task_id),
            auth=es_auth
        )
        completed = status_req.json()['completed']
        if completed:
            sync_lock.acquire()
            completed_slices += 1
            pb_reindexed.update(completed_slices)
            sync_lock.release()
            failures = status_req.json()['response']['failures']
            for failure_i in failures:
                print(failure_i, file=sys.stderr)
            sys.stderr.flush()

        if time.time() - req_start_time > slice_reindex_timeout:
            print('SLICE {0} TIMED OUT'.format(slice_index), file=sys.stderr)
            sys.stderr.flush()
            break
    return completed


future_results = []
with ThreadPoolExecutor(max_workers=6) as executor:
    for i in range(num_slices):
        if not stop_reindex:
            task_result = executor.submit(reindex_slice, i)
            future_results.append(task_result)

for fr_i in future_results:
    is_slice_completed = fr_i.result()





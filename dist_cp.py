from os import walk
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from blessings import Terminal
from progressbar import ProgressBar, Counter, Bar, Percentage, ETA
import atexit
import time
from threading import Lock, Semaphore

t_ini = -time.time()

PROGRESS_BAR_IDX = 0

term = Terminal()


def get_new_progressbar(name, max_val=1) -> ProgressBar:
    global PROGRESS_BAR_IDX
    if PROGRESS_BAR_IDX == 0:
        print(term.clear)
    writer = Writer((0, PROGRESS_BAR_IDX))
    p_bar = ProgressBar(widgets=[name + ': ', Counter(format='%(value)d out of %(max_value)d'), ' ', Percentage(), ' ', Bar(), ' ', ETA()],
                        fd=writer, max_value=max_val).start(max_value=max_val)
    PROGRESS_BAR_IDX += 1
    PROGRESS_BAR_IDX %= 50
    if PROGRESS_BAR_IDX == 0:
        PROGRESS_BAR_IDX += 1
    return p_bar


def write_after_progress_bars():
    print(term.move(PROGRESS_BAR_IDX, 0)+'\n')


########################################################################################################################


class Writer(object):
    """Create an object with a write method that writes to a
    specific place on the screen, defined at instantiation.
    This is the glue between blessings and progressbar.
    """
    def __init__(self, location):
        """
        Input: location - tuple of ints (x, y), the position
        of the bar in the terminal
        """
        self.location = location

    def write(self, string):
        with term.location(*self.location):
            print(string)


def on_exit(signal, frame):
    write_after_progress_bars()

atexit.register(on_exit, *[None, None])

params = sys.argv

orig_dir = sys.argv[1]
dest_dir = sys.argv[2]

pool = ThreadPoolExecutor(32)
pool_semaphore = Semaphore(32)


progressbar_md = {}


def copy_file(from_f, to_dir):
    global cur_counts
    exit_code = subprocess.call(
        'cp {0} {1}'.format(from_f, to_dir),
        shell=True
    )
    if exit_code != 0:
        raise Exception(exit_code)
    return to_dir


def update_pb(to_dir_from_future):
    global progressbar_md, pool, pool_semaphore
    pb_md = progressbar_md[to_dir_from_future.result()]
    pb_md['lock'].acquire()
    pb_md['cur_count'] += 1
    if pb_md['cur_count'] == pb_md['total']:
        pb_md['progressbar'].finish()
    else:
        pb_md['progressbar'].update(pb_md['cur_count'])
    pb_md['lock'].release()
    time.sleep(1)
    pool_semaphore.release()


def copy_files():
    global progressbar_md, pool, pool_semaphore
    total_dir_count = 0
    for (dirpath, dirnames, filenames) in walk(orig_dir):
        total_dir_count += 1

    over_all_pb = get_new_progressbar('COMPLETED DIRECTORIES', total_dir_count)
    over_all_pb.start()
    dirs_done = 0
    for (dirpath, dirnames, filenames) in walk(orig_dir):

        ec = subprocess.call(
            'mkdir -p {0}'.format(os.path.join(dest_dir, os.path.relpath(dirpath, orig_dir))),
            shell=True
        )
        if ec != 0:
            print(ec)
        if len(filenames) > 0:
            to_dir = os.path.join(dest_dir, os.path.relpath(dirpath, orig_dir))
            total_count = len(filenames)
            pb = get_new_progressbar(to_dir, total_count)
            progressbar_md[to_dir] = {
                'total': total_count,
                'cur_count': 0,
                'lock': Lock(),
                'progressbar': pb
            }
            pb.start()

            for file in filenames:
                from_file = os.path.join(dirpath, file)
                pool_semaphore.acquire()
                future = pool.submit(copy_file, from_file, to_dir)
                future.add_done_callback(update_pb)
        dirs_done += 1
        over_all_pb.update(dirs_done)
    over_all_pb.finish()

    pool.shutdown(wait=True)

copy_files()
write_after_progress_bars()
print('TOTAL TIME: {0}'.format((time.time()+t_ini)))
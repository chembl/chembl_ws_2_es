from blessings import Terminal
from progressbar import ProgressBar, Counter, Bar, Percentage, ETA
import glados.es.ws2es.signal_handler as signal_handler
import atexit
from wrapt.decorators import synchronized
import os.path
import sys
import traceback

PROGRESS_BAR_IDX = 0

TERM = None

PROGRESS_BAR_REQUESTED = False

PROGRESS_BAR_BASE_PATH = None


def set_progressbar_out_path(progress_bar_out):
    global PROGRESS_BAR_BASE_PATH
    if progress_bar_out is not None:
        if not os.path.exists(progress_bar_out):
            try:
                os.makedirs(progress_bar_out)
            except:
                traceback.print_exc()
                print('ERROR: {0} is an invalid path for progress bar output.'.format(progress_bar_out), file=sys.stderr)
                sys.exit(1)
        if not os.path.isdir(progress_bar_out):
            print('ERROR: {0} is not a directory.'.format(progress_bar_out), file=sys.stderr)
            sys.exit(1)
        PROGRESS_BAR_BASE_PATH = progress_bar_out

        testing_string = 'Oh yeah! Progress bar testing!'
        test_file_path = os.path.join(PROGRESS_BAR_BASE_PATH, 'test-progress-bar-writing.txt')
        with open(test_file_path, 'w') as file:
            file.write(testing_string)
        with open(test_file_path, 'r') as file:
            lines = file.readlines()
            if lines[0] != testing_string:
                raise Exception('ERROR: Output path for progress bars does not write correctly')
        os.remove(test_file_path)
    else:
        print('WARNING: Attempt to set progress bar out directory with None value.', file=sys.stderr)


@synchronized
def get_new_progressbar(name, max_val=1) -> ProgressBar:
    global PROGRESS_BAR_IDX, PROGRESS_BAR_REQUESTED, TERM, PROGRESS_BAR_BASE_PATH
    if PROGRESS_BAR_IDX == 0:
        if PROGRESS_BAR_BASE_PATH is not None and isinstance(PROGRESS_BAR_BASE_PATH, str):
            # validation made on the set progress bar
            pass
        else:
            TERM = Terminal()
            signal_handler.add_termination_handler(on_exit)
            atexit.register(on_exit, *[None, None])
            print(TERM.clear)
        PROGRESS_BAR_REQUESTED = True
    if PROGRESS_BAR_BASE_PATH is not None and isinstance(PROGRESS_BAR_BASE_PATH, str):
        writer = FilePBWriter(os.path.join(PROGRESS_BAR_BASE_PATH, '{0}.pb'.format(PROGRESS_BAR_IDX)))
    else:
        writer = Writer((0, PROGRESS_BAR_IDX))
    p_bar = ProgressBar(widgets=[name + ': ', Counter(format='%(value)d out of %(max_value)d'), ' ', Percentage(), ' ',
                                 Bar(), ' ', ETA()],
                        fd=writer, max_value=max_val).start(max_value=max_val)
    PROGRESS_BAR_IDX += 1

    return p_bar


def on_exit(signal, frame):
    write_after_progress_bars()


def write_after_progress_bars():
    global TERM
    if PROGRESS_BAR_REQUESTED:
        print(TERM.move(PROGRESS_BAR_IDX, 0) + '\n')


########################################################################################################################

class FilePBWriter(object):

    file_path = None

    def __init__(self, file_path):
        self.file_path = file_path
        self.write('--WAITING-FOR-PROGRESSBAR--')

    def write(self, string):
        with open(self.file_path, 'w') as file:
            file.truncate()
            file.write(string)


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
        global TERM
        with TERM.location(*self.location):
            print(string)


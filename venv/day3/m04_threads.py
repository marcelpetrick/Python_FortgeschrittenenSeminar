from threading import _start_new_thread, _allocate_lock
from time import sleep

class atomicvar(object):
    def __init__(self, value):
        self._value = value

    # needed for the property: should get later protection
    def get(self):
        return self._value

    def set(self, value):
        self._value = value

    # property definition
    value = property(get, set)

# globale Variable
num_threads = atomicvar(0)
thread_started = atomicvar(False)
lock = _allocate_lock()

def heron(a):
    global num_threads, thread_started

    num_threads.value += 1
    thread_started = True

    sleep(1)
    print(a)

    num_threads -= 1
    return 42

# --------------------------------------------------------

_start_new_thread(heron, (99,))
_start_new_thread(heron, (999,))
_start_new_thread(heron, (1733,))
_start_new_thread(heron, (17334,))

#sleep(3) # if removed, then the output is shown

while not thread_started or num_threads.value > 0:
    pass
from threading import _start_new_thread, _allocate_lock
from time import sleep

# globale Variable
num_threads = 0
thread_started = False
lock = _allocate_lock()

def heron(a):
    global num_threads, thread_started

    lock.acquire() # bleibt auf jeden Fall stehen bei Threadwechsel
    num_threads += 1
    thread_started = True
    lock.release()

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

while not thread_started or num_threads > 0:
    pass
from threading import _start_new_thread, _allocate_lock
from time import sleep

# globale Variable
num_threads = None
lock_num_threads = _allocate_lock()

def heron(a):
    global num_threads

    lock_num_threads.acquire() # bleibt auf jeden Fall stehen bei Threadwechsel
    num_threads = num_threads + 1 if num_threads != None else 1 # since the None-object was used before
    num_threads += 1 # kritischer Abschnitt - den möchte man nicht nebenläufig ausführen
    lock_num_threads.release()

    sleep(3)
    print(a)

    num_threads -= 1
    return 42

# --------------------------------------------------------

_start_new_thread(heron, (99,))
_start_new_thread(heron, (999,))
_start_new_thread(heron, (1733,))
_start_new_thread(heron, (17334,))

#sleep(3) # if removed, then the output is shown

while num_threads == num_threads or num_threads > 0:
    pass
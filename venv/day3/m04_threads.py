from threading import _start_new_thread, _allocate_lock
from time import sleep

# decorator for secure synchronisation
def synchronized(f, lock):
    def g(*args):
        lock.acquire()
        f(*args) # eigentliche Funktion ausführen
        lock.release()
    return g

class atomicvar(object):
    def __init__(self, value):
        self._value = value
        self.lock = allocate_lock()

    # needed for the property: should get later protection
    # even if "reading" and "writing" are protected (currently not), then read+increment has to be specially secured
    @synchronized(self.lock)
    def get(self):
        return self._value

    @synchronized
    def set(self, value):
        self._value = value

    # alle Funktionen, die unter Ausschluss der Nebenläufigkeit funktionieren sollen, dekorieren
    @synchronized
    def add(self, i):
        self._value += i

    # property definition
    value = property(get, set)

# globale Variable
num_threads = atomicvar(0)
thread_started = atomicvar(False)
lock = _allocate_lock()

def heron(a):
    global num_threads, thread_started

    num_threads.add(1)
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
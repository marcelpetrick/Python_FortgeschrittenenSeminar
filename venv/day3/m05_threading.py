from threading import Thread, Lock
from time import sleep

class mein_thread(Thread):
    num_threads = 0
    thread_started = False
    lock = Lock()

    def __init__(self, a):
        Thread.__init__(self)  #bei wichtiger Initialisierungsarbeit relevant diesen aufzurufen
        self.a = a

    # nebenläufig auszuführend
    def run(self):
        mein_thread.lock.acquire()
        mein_thread.num_threads += 1
        mein_thread.thread_started = True
        mein_thread.lock.release()

        sleep(1)
        print(self.a)

        mein_thread.lock.acquire()
        mein_thread.num_threads -= 1
        mein_thread.lock.release()
        return 42

# --------------------------------------------------------
threadList = [mein_thread(99),
    mein_thread(999),
    mein_thread(1733),
    mein_thread(17334),
]

# start all the threads
for elem in threadList:
    elem.start()

while not mein_thread.thread_started or mein_thread.num_threads > 0:
    pass
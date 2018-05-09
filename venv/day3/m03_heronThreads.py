from threading import _start_new_thread

num_threads = 0


def heron(a):
    global num_threads
    num_threads += 1

    sleep(3)

    num_threads -= 1
    return 42

# --------------------------------------------------------

_start_new_thread(heron, (99,))
_start_new_thread(heron, (999,))
_start_new_thread(heron, (1733,))
_start_new_thread(heron, (17334,))

while num_threads > 0:
    pass
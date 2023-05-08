import queue

q = queue.Queue()
for i in [1] * 10:
    q.put(i)
print(q.qsize())
print(q)
while not q.empty():
    print(q.get())

# ######################################################################################################################
import queue
import threading

q = queue.Queue()


def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()


# turn-on the worker thread
threading.Thread(target=worker, daemon=True).start()

# send thirty task requests to the worker
for item in range(30):
    q.put(item)
print('All task requests sent\n', end='')

# block until all tasks are done
q.join()
print('All work completed')

# 多进程#################################################################################################################
from multiprocessing import Process


def f(name):
    print('hello', name)


if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

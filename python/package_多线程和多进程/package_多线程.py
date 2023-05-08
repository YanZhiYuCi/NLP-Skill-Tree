import queue
import threading

q = queue.Queue()


def worker(name):
    while True:
        item = q.get()
        print('name:{}'.format(name))
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()


# turn-on the worker thread
threading.Thread(target=worker, args=('bob',), daemon=True).start()

# send thirty task requests to the worker
for item in range(30):
    q.put(item)
print('All task requests sent')

# block until all tasks are done
q.join()
print('All work completed')

import queue

q = queue.Queue()
data = list(range(10))
for i in data:
    q.put(i)
print('q.qsize:{}'.format(q.qsize()))
while not q.empty():
    print('q.get:{}'.format(q.get()))

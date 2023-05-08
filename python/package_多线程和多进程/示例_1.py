from queue import Queue
import time
import threading

q = Queue(maxsize=0)


def product(name):
    count = 1  # 第几个
    while True:
        q.put('气球兵{}'.format(count))  # 元素个数为1
        print('q.qsize()):{}'.format(q.qsize()))
        print('{}训练气球兵{}只'.format(name, count))
        count += 1
        time.sleep(1)


def consume(name):
    while True:
        print('{}使用了{}'.format(name, q.get()))
        time.sleep(5)
        print('q.qsize()):{}'.format(q.qsize()))
        q.task_done()  # 之后元素会减一
        print('q.qsize()):{}'.format(q.qsize()))


t1 = threading.Thread(target=product, args=('小黄',))
t2 = threading.Thread(target=consume, args=('小郭',))
t3 = threading.Thread(target=consume, args=('小晁',))

t1.start()
t2.start()
t3.start()

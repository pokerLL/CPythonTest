import time
import threading
from queue import Queue

def target(queue):
    while True:
        task = queue.get()
        if task == "stop":
            queue.task_done()
            break

        task()
        queue.task_done()

def do_task():
    for i in range(5):
        print('running thread-{}:{}'.format(threading.get_ident(), i))
        time.sleep(1)


class MyQueue(Queue):
    def close(self):
        for i in range(self.maxsize):
            self.put("stop")

def custome_pool(task_func, max_workers):
    queue = MyQueue(max_workers)
    for n in range(max_workers):
        t = threading.Thread(target=task_func, args=(queue,))
        t.daemon = True
        t.start()

    return queue



pool = custome_pool(task_func=target, max_workers=5)

for i in range(10):
    pool.put(do_task)

pool.close()
pool.join()
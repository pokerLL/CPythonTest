from multiprocessing import Process, current_process
import logging
import os
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-15s - %(levelname)s - %(message)s'
)


def run():
    time.sleep(30)
    logging.info('exit grandchild process %s', current_process().pid)
    os._exit(3)


def worker():
    p = Process(target=run)
    p.start()
    logging.info('exit worker process %s, grandchild is %s',
                 current_process().pid, p.pid)
    os._exit(1)


p = Process(target=worker)
p.start()
p.join()
time.sleep(100)
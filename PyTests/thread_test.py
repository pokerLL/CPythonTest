import threading

class MyClass:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.lock = threading.RLock()

    def update(self, thread_name):
        print("Waiting: ", thread_name)
        self.lock.acquire()
        try:
            print("Acquired: ", thread_name)
            self.a += 1
            self.b += 1
            print("a =", self.a, "b =", self.b)
        finally:
            self.lock.release()
            print("Released: ", thread_name)

if __name__ == "__main__":
    c = MyClass()
    t1 = threading.Thread(target=c.update, args=("Thread-1",))
    t2 = threading.Thread(target=c.update, args=("Thread-2",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
"""
Waiting:  Thread-1
Acquired:  Thread-1
Waiting:  Thread-2
a = 2 b = 3
Released:  Thread-1
Acquired:  Thread-2
a = 3 b = 4
Released:  Thread-2
"""
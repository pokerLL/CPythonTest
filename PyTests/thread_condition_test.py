import threading, time

class Hider(threading.Thread):
    def __init__(self, cond, name):
        super(Hider, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        print("hider 0")
        time.sleep(1)  #确保先运行Seeker中的方法
        print("hider 1")
        self.cond.acquire()

        print(self.name + ': 我已经把眼睛蒙上了')
        self.cond.notify()
        print("hider 2")
        self.cond.wait()
        print(self.name + ': 我找到你了哦 ~_~')
        self.cond.notify()
        print("hider 3")

        self.cond.release()
        print(self.name + ': 我赢了')

class Seeker(threading.Thread):
    def __init__(self, cond, name):
        super(Seeker, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        print("seeker 0")
        self.cond.acquire()
        print("seeker 1")
        self.cond.wait()
        print(self.name + ': 我已经藏好了，你快来找我吧')
        self.cond.notify()
        print("seeker 2")
        self.cond.wait()
        print("seeker 3")
        self.cond.release()
        print(self.name + ': 被你找到了，哎~~~')

cond = threading.Condition()
seeker = Seeker(cond, 'seeker')
hider = Hider(cond, 'hider')
seeker.start()
hider.start()

"""
seeker 0hider 0

seeker 1
hider 1
hider: 我已经把眼睛蒙上了
hider 2
seeker: 我已经藏好了，你快来找我吧
seeker 2
hider: 我找到你了哦 ~_~
hider 3
hider: 我赢了seeker 3
seeker: 被你找到了，哎~~~
"""
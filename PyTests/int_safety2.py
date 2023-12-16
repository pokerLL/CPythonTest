from threading import Thread, Lock

number = 0

def target():
    global number
    for _ in range(1000000):
        number += 1

thread_01 = Thread(target=target)
thread_02 = Thread(target=target)
thread_01.start()
thread_02.start()

thread_01.join()
thread_02.join()

print(number)
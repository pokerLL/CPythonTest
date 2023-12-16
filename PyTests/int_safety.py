# 测试内建对象int是否是线程安全的

import threading

n = 0

def foo():
    global n
    n += 1

threads = []
for i in range(1000):
    t = threading.Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(n)

"""
>>> dis.dis("n=1;n+=1;")
  1           0 LOAD_CONST               0 (1)
              2 STORE_NAME               0 (n)
              4 LOAD_NAME                0 (n)
              6 LOAD_CONST               0 (1)
              8 INPLACE_ADD
             10 STORE_NAME               0 (n)
             12 LOAD_CONST               1 (None)
             14 RETURN_VALUE

TODO:
在3.7和3.10下多次运行结果都是正确的
但是从dis的情况来看 n+=1 似乎不是原子操作,因此是会发生race condition的,结果不应该一直是正确的

"""
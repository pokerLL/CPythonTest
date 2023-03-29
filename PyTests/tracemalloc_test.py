import tracemalloc

# 开始跟踪内存分配情况
tracemalloc.start()

# 执行一些代码，分配一些内存
s = ' ' * 1000000
lst = [i for i in range(100000)]

# 获取当前内存使用量
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024} MB")
print(f"Peak memory usage: {peak / 1024 / 1024} MB")

# 获取当前的内存快照并输出统计信息
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)

"""
Current memory usage: 4.403904914855957 MB
Peak memory usage: 4.404065132141113 MB
[ Top 10 ]
c:/Workspace/Program/CPythonTest/PyTests/tracemalloc_test.py:8: size=3532 KiB, count=99744, average=36 B
c:/Workspace/Program/CPythonTest/PyTests/tracemalloc_test.py:7: size=977 KiB, count=2, average=489 KiB
c:/Workspace/Program/CPythonTest/PyTests/tracemalloc_test.py:12: size=72 B, count=1, average=72 B
c:/Workspace/Program/CPythonTest/PyTests/tracemalloc_test.py:11: size=56 B, count=2, average=28 B
"""
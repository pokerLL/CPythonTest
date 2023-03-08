t = [(1, 2), (3, 4), (5, 6), (7, 8)]
for idx,(v1,v2) in enumerate(t):
    print(idx,v1,v2,sep=' ')
"""
0 1 2
1 3 4
2 5 6
3 7 8
"""

for idx,v1,v2 in enumerate(t):
    print(idx,v1,v2,sep=' ')
"""
Traceback (most recent call last):
  File "d:/Program/Workspace/CPythonTest/PyTests/enumerate_test.py", line 11, in <module>
    for idx,v1,v2 in enumerate(t):
ValueError: not enough values to unpack (expected 3, got 2)
"""
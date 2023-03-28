funcs = [lambda x : x+n for n in range(5)]
for f in funcs:
    print(f(0))
"""
4
4
4
4
4
"""

funcs = [lambda x,n=n : x+n for n in range(5)]
for f in funcs:
    print(f(0))
"""
0
1
2
3
4
"""
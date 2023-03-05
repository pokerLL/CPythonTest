t1 = (1,2,3)
t2 = tuple(t1)
t3 = t1[:]
print(t1 == t2)
print(t1 is t2)
print(id(t1),'  ',id(t2))
"""
True
True
2207179699928    2207179699928
"""

print(t1 == t3)
print(t1 is t3)
print(id(t1),'  ',id(t3))
"""
True
True
2207179699928    2207179699928
"""

# print(help(tuple))
"""

class tuple(object)
 |  tuple(iterable=(), /)
 |
 |  Built-in immutable sequence.
 |
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |
 |  If the argument is a tuple, the return value is the same object.  <-
"""
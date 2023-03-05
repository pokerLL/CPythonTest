"""
>>> t = (1, 2, [30, 40])
>>> t[2] += [50, 60]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t
(1, 2, [30, 40, 50, 60])
>>> import dis
>>> dis.dis('t[2]+=[100]')
  1           0 LOAD_NAME                0 (t)
              2 LOAD_CONST               0 (2)
              4 DUP_TOP_TWO
              6 BINARY_SUBSCR
              8 LOAD_CONST               1 (100)
             10 BUILD_LIST               1
             12 INPLACE_ADD
             14 ROT_THREE
             16 STORE_SUBSCR
             18 LOAD_CONST               2 (None)
             20 RETURN_VALUE
>>> dis.dis('t[2].append(100)') 
  1           0 LOAD_NAME                0 (t)
              2 LOAD_CONST               0 (2)
              4 BINARY_SUBSCR
              6 LOAD_METHOD              1 (append)
              8 LOAD_CONST               1 (100)
             10 CALL_METHOD              1
             12 RETURN_VALUE
>>> t[2].append(100) 
>>> t
(1, 2, [30, 40, 50, 60, 100])
>>>
"""

t = (1, 2, [30, 40])
try:
    t[2] += [50, 60]
except Exception as e:
    print("CATCH: ",e)
print(t)
# CATCH:  'tuple' object does not support item assignment
# (1, 2, [30, 40, 50, 60])


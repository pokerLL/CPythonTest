it = iter(list(range(10)))

print(f'2 in it: {2 in it}')    # True

print(f'next(it): {next(it)}')  # 3

import dis

print(f'{dis.dis("2 in it")}')
""" 
  0           0 RESUME                   0

  1           2 LOAD_CONST               0 (2)
              4 LOAD_NAME                0 (it)
              6 CONTAINS_OP              0
              8 RETURN_VALUE
"""

print('======================================')

print(f'{dis.dis("for i in [1,2,3]: pass")}')
""" 
  0           0 RESUME                   0

  1           2 LOAD_CONST               0 ((1, 2, 3))
              4 GET_ITER
        >>    6 FOR_ITER                 2 (to 12)
              8 STORE_NAME               0 (i)
             10 JUMP_BACKWARD            3 (to 6)
        >>   12 LOAD_CONST               1 (None)
             14 RETURN_VALUE
"""
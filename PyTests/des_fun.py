class A:
    def fun(*args,**kwargs):
        pass

def fun(*args,**kwargs):
        pass

a = A()

a.fun()

A.fun()

"""
>>> import des_fun as df
>>> df.a
<des_fun.A object at 0x0000027F3C7CDA48>
>>> df.A
<class 'des_fun.A'>
>>> df.A.fun
<function A.fun at 0x0000027F3C795E58>
>>> df.a.fun 
<bound method A.fun of <des_fun.A object at 0x0000027F3C7CDA48>>
>>> dis.dis(compile('df.a.fun()','','exec')) 
  1           0 LOAD_NAME                0 (df)
              2 LOAD_ATTR                1 (a)
              4 LOAD_METHOD              2 (fun)
              6 CALL_METHOD              0
              8 POP_TOP
             10 LOAD_CONST               0 (None)
             12 RETURN_VALUE
>>> dis.dis(compile('df.A.fun()','','exec')) 
  1           0 LOAD_NAME                0 (df)
              2 LOAD_ATTR                1 (A)
              4 LOAD_METHOD              2 (fun)
              6 CALL_METHOD              0
              8 POP_TOP
             10 LOAD_CONST               0 (None)
             12 RETURN_VALUE
>>> dis.dis(compile('df.fun()','','exec'))   
  1           0 LOAD_NAME                0 (df)
              2 LOAD_METHOD              1 (fun)
              4 CALL_METHOD              0
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
>>> dis.dis(compile('df.fun','','exec'))   
  1           0 LOAD_NAME                0 (df)
              2 LOAD_ATTR                1 (fun)
              4 POP_TOP
              6 LOAD_CONST               0 (None)
              8 RETURN_VALUE
>>> dis.dis(compile('df.A.fun','','exec')) 
  1           0 LOAD_NAME                0 (df)
              2 LOAD_ATTR                1 (A)
              4 LOAD_ATTR                2 (fun)
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
>>> dis.dis(compile('df.a.fun','','exec')) 
  1           0 LOAD_NAME                0 (df)
              2 LOAD_ATTR                1 (a)
              4 LOAD_ATTR                2 (fun)
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
"""

"""
>>> from des_fun import *
>>> dis.dis(compile('A.fun()','','exec'))    
  1           0 LOAD_NAME                0 (A)
              2 LOAD_METHOD              1 (fun)
              4 CALL_METHOD              0
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
>>> dis.dis(compile('a.fun()','','exec')) 
  1           0 LOAD_NAME                0 (a)
              2 LOAD_METHOD              1 (fun)
              4 CALL_METHOD              0
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
>>> dis.dis(compile('fun()','','exec'))   
  1           0 LOAD_NAME                0 (fun)
              2 CALL_FUNCTION            0
              4 POP_TOP
              6 LOAD_CONST               0 (None)
              8 RETURN_VALUE
>>> dis.dis(compile('fun','','exec'))      
  1           0 LOAD_NAME                0 (fun)
              2 POP_TOP
              4 LOAD_CONST               0 (None)
              6 RETURN_VALUE
>>> dis.dis(compile('A.fun','','exec'))    
  1           0 LOAD_NAME                0 (A)
              2 LOAD_ATTR                1 (fun)
              4 POP_TOP
              6 LOAD_CONST               0 (None)
              8 RETURN_VALUE
>>> dis.dis(compile('a.fun','','exec'))    
  1           0 LOAD_NAME                0 (a)
              2 LOAD_ATTR                1 (fun)
              4 POP_TOP
              6 LOAD_CONST               0 (None)
              8 RETURN_VALUE
"""

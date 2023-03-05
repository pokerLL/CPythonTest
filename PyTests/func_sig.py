"""
>>> from func_sig import fun 
>>> from inspect import signature
>>> sig = signature(fun) 
>>> sig
<Signature (text, max_len: int = 180, *args, **kwargs)>
>>> str(sig) 
'(text, max_len: int = 180, *args, **kwargs)'
>>> for name,param in sig.parameters.items():
...     print(param.kind,':',name,'=',param.default)
... 
POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
POSITIONAL_OR_KEYWORD : max_len = 180
VAR_POSITIONAL : args = <class 'inspect._empty'>
VAR_KEYWORD : kwargs = <class 'inspect._empty'>
"""

"""
>>> from func_sig import fun 
>>> fun.__annotations__       
{'max_len': <class 'int'>}
>>> from func_sig import fun2
>>> fun2.__annotations__
{'text': <class 'str'>, 'max_len': 'int > 0'}
"""

def fun(text, max_len: int = 180, *args, **kwargs):
    pass

def fun2(text:str, max_len:"int > 0"=100):
    pass
"""
>>> s = "str.{}".format(b'bytes') 
>>> print(s) 
str.b'bytes'
>>> b = "bytes.{}".format("str") 
>>> b
'bytes.str'
>>> b = b"bytes.{}".format("str")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'bytes' object has no attribute 'format'
>>> b = b"bytes.{}".format(b"str") 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'bytes' object has no attribute 'format'
>>> b = b"bytes.{}"%(b"str")       
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: not all arguments converted during bytes formatting
>>> b = b"bytes.%s"%(b"str") 
>>> b
b'bytes.str'
>>>
>>> s = "str.{}".format(b'bytes')  
>>> s
"str.b'bytes'"
>>> b = b"bytes.%s" % (b"str") 
>>> b
b'bytes.str'
>>> b = b"bytes.{}".format(b"str")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'bytes' object has no attribute 'format'
>>> b = b"bytes.%s"%("str")        
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: %b requires a bytes-like object, or an object that implements __bytes__, not 'str'     
>>>
"""
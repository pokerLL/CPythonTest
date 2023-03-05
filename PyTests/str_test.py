"""
>>> s = "cafe" 
>>> s
'cafe'
>>> b = s.encode('utf-8') 
>>> b
b'cafe'
>>> s2 = b.decode('utf-8')
>>> s2
'cafe'
>>> s2 == s 
True
>>> sb = bytes(s,encoding='utf-8') 
>>> sb
b'cafe'
>>> sb == b
True
>>> sbarr = bytearray(b) 
>>> sbarr
bytearray(b'cafe')
>>> len(sbarr) 
4
>>> sbarr[-1:] 
bytearray(b'e')
>>>
"""
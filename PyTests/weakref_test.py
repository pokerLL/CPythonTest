"""
>>> import weakref
>>> l = {1,2}  
>>> wref = weakref.ref(l)
>>> wref
<weakref at 0x000001B54726C8B8; to 'set' at 0x000001B547230908>
>>> wref()
{1, 2}
>>> l.add(3) 
>>> wref()   
{1, 2, 3}
>>> l = {4,5,6} 
>>> wref()      
{1, 2, 3} # 此处和下面都还能看到{1,2,3}的原因时控制台会自动把_变量指向上一条语句的执行结果
>>> wref() is None
False # 
>>> wref() is None
True
>>> wref()
>>> 
"""

"""
>>> a = {1} 
>>> a
{1}
>>> _
{1}
"""
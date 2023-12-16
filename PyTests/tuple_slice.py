t = (1,2,3,4,5,6,7)

print(tuple(t) is t)
print(t[:] is t)
print(t[1:-1] is t)
""" 
True
True
False
"""
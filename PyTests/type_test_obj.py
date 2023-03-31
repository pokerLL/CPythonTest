print(type(int))            # <class 'type'>
print(type(type(int)))      # <class 'type'>
print(type(object))         # <class 'type'>
print(int.__bases__)        # (<class 'object'>,)
print(type.__bases__)       # (<class 'object'>,)
print(object.__bases__)     # ()
def decorator(func):
    def inner(*args,**kwargs):
        print("inner",locals())
        args[0].ALL = 10086
        func(*args,**kwargs)

    return inner

class A:
    @classmethod
    @decorator
    def decdclsfun(*args,**kwargs):
        print(args[0].ALL)
        print("clsfun", "   ", locals())


    @staticmethod
    def stafun(*args,**kwargs):
        print("stafun", "   ", locals())
    
    
    def insfun(*args,**kwargs):
        print("insfun", "   ", locals())
        if len(args):
            sm = args[0]
            print(sm,type(sm))
    
    @classmethod
    def clsmethod(*args,**kwargs):
        print("cleanclsmethod", "   ", locals())
    

def fun(*args,**kwargs):
    print("fun", "   ", locals())



# A.decdclsfun()  # inner {'args': (), 'kwargs': {}, 'func': <function A.clsfun at 0x000001B621C46048>}
#                 # 10086
#                 # decdclsfun     {'args': (<class '__main__.A'>,), 'kwargs': {}}

# A.stafun()      # stafun     {'args': (), 'kwargs': {}}
# A.insfun()      # insfun     {'args': (), 'kwargs': {}}
# A.clsmethod()   # clsmethod     {'args': (<class '__main__.A'>,), 'kwargs': {}}

a = A()
# a.decdclsfun()  # inner {'args': (), 'kwargs': {}, 'func': <function A.clsfun at 0x000001B621C46048>}
#                 # 10086
#                 # clsfun     {'args': (<class '__main__.A'>,), 'kwargs': {}}
# a.stafun()      # stafun     {'args': (), 'kwargs': {}}
# a.insfun()      # insfun     {'args': (<__main__.A object at 0x000001F7515BC248>,), 'kwargs': {}}
#                 # <__main__.A object at 0x000001F7515BC248> <class '__main__.A'>
# a.clsmethod()   # clsmethod     {'args': (<class '__main__.A'>,), 'kwargs': {}}

fun()           # fun     {'args': (), 'kwargs': {}}
# a.fun()
A.fun()
from utils import debug
class A:
    
    def __init__(self) -> None:
        self.p = 1

    @debug
    def __getattribute__(self, item):
        """
        属性查找首先调用__getattribute__
        """
        return object.__getattribute__(self, item)
    
    @debug
    def __getattr__(self,item):
        '''
        当属性不存在时则调用__getattr__
        '''
        return "NOTHING"
        # return object.__getattr__(self, item)

    @debug
    def fun(self):
        pass

def main():
    a = A()
    a.fun()
    '''
Calling __getattribute__
    with args: (<__main__.A object at 0x00000235B01113A0>, 'fun')
    kwargs: {}
    local variables: {'a': <__main__.A object at 0x00000235B01113A0>}
Calling fun
    with args: (<__main__.A object at 0x00000235B01113A0>,)
    kwargs: {}
    local variables: {'a': <__main__.A object at 0x00000235B01113A0>}
    '''
    a.p
    '''
Calling __getattribute__
    with args: (<__main__.A object at 0x00000235B01113A0>, 'p')
    kwargs: {}
    local variables: {'a': <__main__.A object at 0x00000235B01113A0>}
    '''
    a.nothing
    '''
Calling __getattribute__
    with args: (<__main__.A object at 0x00000235B01113A0>, 'nothing')
    kwargs: {}
    local variables: {'a': <__main__.A object at 0x00000235B01113A0>}
Calling __getattr__
    with args: (<__main__.A object at 0x00000235B01113A0>, 'nothing')
    kwargs: {}
    local variables: {'a': <__main__.A object at 0x00000235B01113A0>}
    '''


if __name__ == '__main__':
    main()
    print(hasattr(object ,'__getattr__')) # False
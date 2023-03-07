
# BEGIN DESCR_KINDS

### auxiliary functions for display only ###

def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]

def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))

def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))


### essential classes for this example ###

class Overriding:  # <1>
    """a.k.a. data descriptor or enforced descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)  # <2>

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:  # <3>
    """an overriding descriptor without ``__get__``"""

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:  # <4>
    """a.k.a. non-data or shadowable descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:  # <5>
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):  # <6>
        print('-> Managed.spam({})'.format(display(self)))

# END DESCR_KINDS

man = Managed()

# print(man.over_no_get)      # <__main__.OverridingNoGet object at 0x000002009326F6C8>
# man.over_no_get = "MMMMM"   # -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, <str object>)
# print(man.over_no_get)      # <__main__.OverridingNoGet object at 0x000002009326F6C8>
# man.__dict__["over_no_get"] = "man-over_no_get"
# print(man.over_no_get)      # man-over_no_get
# man.over_no_get = "MMMMM"   # -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, <str object>)
# print(man.over_no_get)      # man-over_no_get


# print(man.non_over) # -> NonOverriding.__get__(<NonOverriding object>, <Managed object>, <class Managed>)
#                     # None
# man.non_over = "NNNNN"
# print(vars(man))    # {'non_over': 'NNNNN'}
# print(man.non_over) # NNNNN
# man.__dict__["non_over"] = "man-non_over"
# print(man.non_over) # man-non_over
# man.non_over = "NNNNN" 
# print(man.non_over) # NNNNN
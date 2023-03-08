from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        # if not __debug__:
        #     return func

        # Map function argument names to supplied types
        sig = signature(func)
        sigb = sig.bind_partial(*ty_args, **ty_kwargs)
        bound_types = sigb.arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                            )
            return func(*args, **kwargs)
        return wrapper
    return decorate

@typeassert(int, int)
def add(a, b):
    return a + b

print(add(2, 3)) # Output: 5
print(add(2, "3")) # Output: TypeError: Argument b must be <class 'int'>

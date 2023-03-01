import inspect

def debug(func):
    def wrapper(*args, **kwargs):
        # 获取函数名称
        function_name = func.__name__
        # 获取局部变量
        local_vars = inspect.currentframe().f_back.f_locals
        # 打印函数名和局部变量
        print(
f"""Calling {function_name} 
    with args: {args} 
    kwargs: {kwargs} 
    local variables: {local_vars}
    """)

        return func(*args, **kwargs)
    return wrapper

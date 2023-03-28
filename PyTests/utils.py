import inspect
import time
from datetime import datetime
import os

def debug(func):
    # 在windows上需要使用time.clock() Linux上可以使用process_time()
    # 这里放到闭包空间内做减少判断次数和增加取值消耗直接的权衡
    if os.name == 'nt':
        process_time_func = time.clock
    else:
        process_time_func = time.process_time

    def wrapper(*args, **kwargs):
        # 获取函数名称
        function_name = func.__module__+ '.' +func.__qualname__
        # 获取局部变量
        local_vars = inspect.currentframe().f_back.f_locals
        local_time = datetime.now()
        pref_time_start = time.perf_counter()
        prcoess_time_start = process_time_func()
        resp = func(*args, **kwargs)
        prcoess_time_end = process_time_func()
        pref_time_end = time.perf_counter()
        # 打印各种统计信息
        print(
f"""Calling {function_name} at {local_time} with
    args:\t{args} 
    kwargs: \t{kwargs} 
    local variables:\t{local_vars}
    result:\t{repr(resp)}
    process_time:\t{prcoess_time_end-prcoess_time_start}
    pref_counter_time:\t{pref_time_end-pref_time_start}
""")

        return resp
    return wrapper

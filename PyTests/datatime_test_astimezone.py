import pytz
from datetime import datetime

# 创建一个表示美国纽约时区的pytz时区对象
ny_tz = pytz.timezone('America/New_York')

# 创建一个本地时间的datetime对象
local_time = datetime.now()

# 使用astimezone()方法将本地时间转换为纽约时区时间
ny_time = local_time.astimezone(ny_tz)

# 打印输出本地时间和纽约时区时间
print("Local Time\t:", local_time)
print("NewYork Time\t:", ny_time)

"""
Local Time      : 2023-03-28 17:48:20.417971
NewYork Time    : 2023-03-28 05:48:20.417971-04:00
"""
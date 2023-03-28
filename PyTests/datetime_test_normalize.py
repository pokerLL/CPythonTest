import pytz
from datetime import datetime

# 创建一个表示美国纽约时区的pytz时区对象
ny_tz = pytz.timezone('America/New_York')
utc_tz = pytz.timezone('UTC')

# 创建一个表示纽约时区时间的datetime对象
ny_time = datetime(2023, 3, 28, 10, 30, 0, tzinfo=ny_tz)

# 使用normalize()方法将纽约时区时间转换为UTC时间
utc_time = utc_tz.normalize(ny_time)

# 打印输出纽约时区时间和UTC时间
print("NY Time:", ny_time)
print("UTC Time:", utc_time)

"""
NY Time: 2023-03-28 10:30:00-04:56
UTC Time: 2023-03-28 15:26:00+00:00
"""

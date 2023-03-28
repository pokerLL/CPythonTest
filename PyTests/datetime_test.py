import pytz
from datetime import datetime

local_tz = pytz.timezone('Asia/Shanghai')
utc_tz = pytz.timezone("UTC")
local_time_withtz = datetime.now(local_tz)
utc_time_withtz = datetime.now(utc_tz)
utc_time_utcnow = datetime.utcnow()
local_time_now = datetime.now()

date_str = '2022-03-28 10:30:00'
date_format = '%Y-%m-%d %H:%M:%S'
date_obj = datetime.strptime(date_str, date_format)


"""
>>> local_tz = pytz.timezone('Asia/Shanghai')
>>> utc_tz = pytz.timezone("UTC")
>>> local_time_withtz = datetime.now(local_tz)
>>> local_time_withtz
datetime.datetime(2023, 3, 28, 17, 40, 29, 702833, tzinfo=<DstTzInfo 'Asia/Shanghai' CST+8:00:00 STD>)
>>> utc_time_withtz = datetime.now(utc_tz)
>>> utc_time_withtz
datetime.datetime(2023, 3, 28, 9, 40, 38, 251995, tzinfo=<UTC>)
>>> utc_time_utcnow = datetime.utcnow()
>>> utc_time_utcnow
datetime.datetime(2023, 3, 28, 9, 40, 56, 518353)
>>> local_time_now = datetime.now()
>>> local_time_now
datetime.datetime(2023, 3, 28, 17, 41, 29, 426546)
>>> date_str = '2022-03-28 10:30:00'
>>> date_format = '%Y-%m-%d %H:%M:%S'
>>> date_obj = datetime.strptime(date_str, date_format)
>>> date_obj
datetime.datetime(2022, 3, 28, 10, 30)
"""
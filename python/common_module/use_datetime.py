#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'datetime'
# datetime是Python处理日期和时间的标准库。
from datetime import datetime,timedelta,timezone
# 获取当前日期和时间
print('01.',datetime.now())
# 获取指定日期和时间
print('02.',datetime(2002,9,25,12,30))
# datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
print('03.',datetime.now().timestamp())
# timestamp转换为datetime
print('04.',datetime.fromtimestamp(1509616013))
# timestamp也可以直接被转换到UTC标准时区的时间
print('05.',datetime.utcfromtimestamp(1509616013))
# str转换为datetime
# 注意转换后的datetime是没有时区信息的。
print('06.',datetime.strptime('2017-11-2 00:00:00','%Y-%m-%d %H:%M:%S'))
# datetime转换为str
print('07.',datetime.now().strftime('%a, %b %d %H:%M'))
# datetime加减,需要导入timedelta这个类
print('08.',datetime.now()-timedelta(days=1))
# 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
tz_utc_8=timezone(timedelta(hours=8))
print('09.',datetime.now().replace(tzinfo=tz_utc_8))
# 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。
# 时区转换
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print('10.',utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print('11.',bj_dt)
# astimezone()将bj_dt转换时区为东京时间:
# astimezone()将utc_dt转换时区为东京时间:
print('12.',bj_dt.astimezone(timezone(timedelta(hours=9))))
print('13.',utc_dt.astimezone(timezone(timedelta(hours=9))))
# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
# 注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。

# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
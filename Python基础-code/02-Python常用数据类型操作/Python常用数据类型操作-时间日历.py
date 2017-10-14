

import time


# result = time.time()
# years = result / (24 * 60 * 60 * 365) + 1970
# print(years)
# print(result)
#
#
# result = time.localtime(1404100165.036104)
# print(result)


# 获取格式化的时间
# 	秒 -> 可读时间
# 		import time
# 		time.ctime([seconds])
# 			seconds
# 				可选的时间戳
# 				默认当前时间戳

# t = time.time()
# result = time.ctime(t)
# print(result)



# 	时间元组 -> 可读时间
# 		import time
# 		time.asctime([p_tuple])
# 			p_tuple
# 				可选的时间元组
# 				默认当前时间元组

# time_tuple = time.localtime()
# result = time.asctime(time_tuple)
# print(result)



# 字符串 -> 格式化日期
# 	time.strftime(格式字符串, 时间元组)
# 	例如
# 		time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# 		2017-09-02 17:21:00

# result = time.strftime("%y===%m-%d %H:%M:%S", time.localtime())
# print(result)
#
#
#
#
# pt = time.strptime("17===09-06 08:57:17", "%y===%m-%d %H:%M:%S")
# print(pt)
#
#
# t = time.mktime(pt)
# print(t)
#
# start = time.clock()
# for i in range(0, 10000):
#     print(i)
#
# end = time.clock()
# print(end - start)
#
#
#
#
# while True:
#     result = time.strftime("%y===%m-%d %H:%M:%S", time.localtime())
#     print(result)
#     time.sleep(1)


# import calendar
#
# print(calendar.month(2017, 6))









# import datetime
# t = datetime.datetime.now()
# print(datetime.datetime.today())
#
#
# print(type(t))
# print(t.year)
# print(t.month)
# print(t.day)
#
# print(t.hour)
# print(t.minute)
# print(t.second)







import datetime

# t = datetime.datetime.today()
# result = t + datetime.timedelta(days=7)
# print(t, result)


first = datetime.datetime(2017, 9, 2, 12, 00, 00)
second = datetime.datetime(2017, 9, 3, 12, 00, 00)
# print(first, type(first))


delta = second - first
print(delta, type(delta))
print(delta.total_seconds())

























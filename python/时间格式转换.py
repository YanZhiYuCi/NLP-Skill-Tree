import time
import datetime

st_1 = time.strptime('2019-5-1 10:12:20.1', '%Y-%m-%d %H:%M:%S.%f')
# st_1 = time.strptime('2019-5-1','%Y-%m-%d')
print('st1:{}'.format(st_1))
time_stamp_1 = time.mktime(st_1)  # 转化成时间戳精确到秒级别
print('time_stamp_1:{}'.format(time_stamp_1))

st_2 = time.localtime()  # 当前的本机时间
print('st2:{}'.format(st_2))
time_stamp_2 = time.strftime("%Y-%m-%d %H:%M:%S", st_2)
print('time_stamp_2:{}'.format(time_stamp_2))

dt_1 = datetime.datetime.strptime("2020-06-14 23:03:15.163813", '%Y-%m-%d %H:%M:%S.%f')
dt_1 = datetime.datetime.strptime("2021-08-06 17-05-32", '%Y-%m-%d %H-%M-%S')
print('dt_1:{}'.format(dt_1))
date_stamp_1 = int(time.mktime(dt_1.timetuple()))
print(str(date_stamp_1))

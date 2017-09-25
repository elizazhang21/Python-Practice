import datetime
import time
from datetime import datetime, timedelta

date = '06/21/1995'
date = datetime.strptime(date, '%m/%d/%Y').strftime("%Y%m%d")
print(date)

open_time = '3:00:00 AM'
open_time = datetime.strptime(open_time, '%I:%M:%S %p')
open_time = datetime.strftime(open_time, '%I:%M:%S %p')
print(open_time)


dt = datetime.strptime('2017-09-19 03:00:00','%Y-%m-%d %H:%M:%S')
dtstamp = int(time.mktime(dt.timetuple()))
print(dtstamp)

time1 = 0.125
time1 = timedelta(time1)
print(time1)

date1 = datetime.strptime('06/21/1995','%m/%d/%Y')-timedelta(days=1)
print(date1)
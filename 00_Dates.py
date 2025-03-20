### Dates ###
from datetime import datetime

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

now = datetime.now()

print_date(now)

timestamp = now.timestamp()

# print_date(timestamp)

year2026 =datetime(2026,1,1)
    
print_date(year2026)

from datetime import time

current_time = time(21,23,0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()   

print(current_date.year)
print(current_date.month)
print(current_date.day)




current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)


diff = year2026 - now
print(diff)
diff = year2026.date() - current_date
print(diff)

# diff = year2026.time() - current_time
# print(diff)

from datetime import timedelta

start_timedelta = timedelta(200,100, 100, weeks = 10)
end_time_delta = timedelta(300,100, 100, weeks = 13)

print(end_time_delta - start_timedelta)
print(end_time_delta + start_timedelta)


















































import calendar;
import datetime;
import time;

print(calendar.weekheader(1))

print(calendar.firstweekday())

print(calendar.month(2020, 1))

print(calendar.monthcalendar(2020, 1))

print(calendar.calendar(2020))

dow = calendar.weekday(2020, 3,3)
print(dow)

isLeap = calendar.isleap(2020)
print(isLeap)


how_many_leap_days = calendar.leapdays(2000,2005)
print(how_many_leap_days)

print(datetime.date())
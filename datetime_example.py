import datetime;
ad = "ambuj dubey"
today = datetime.date.today();
todayDT = datetime.datetime.today();
dob = datetime.date(1989,8,6);
print(today);
print(dob);
print(repr(dob))# like type of in js

day_since_birthday = (today - dob).days;
print(day_since_birthday);#1647 9469 11131

# add some(Exa :- 10 more day) day in current day (today)
addTimeDelta = datetime.timedelta(days=10);
print(today + addTimeDelta)

# today month
print(today.month)

# today day
print(today.day)


# today weekdy -> Mon=0 - Sun=6
print(today.weekday())


# today set time
print(datetime.time(9,43,50,10))
#datetime.date(Y-M-D)
#datetime.time(H-M-S-MS)
#atetime.datetime(Y-M-D H-M-S-MS)
print(todayDT.time())

# timedelta
# add some(Exa :- 10 more hour) hour in current time (today)
hour_delta = datetime.timedelta(hours=10);
print(todayDT + hour_delta)


#pip install --user pytz    set Time zone in python
import pytz;
datetime_today_utc = datetime.datetime.now(tz=pytz.UTC);
print(datetime_today_utc);

datetime_today_pacific = datetime_today_utc.astimezone(pytz.timezone('US/Pacific'));
print(datetime_today_pacific);

#print all time zone in python
for tz in pytz.all_timezones:
    print(tz)



#string formatting with dates in python
#1 January 27, 2020
print(datetime_today_pacific.strftime('%B %d, %Y'));

#2 Take input as 'January 27, 2020' and output as '2020-01-27'
datetime_today_str = datetime.datetime.strptime('January 27, 2020','%B %d, %Y')
print(datetime_today_str);
print(repr(datetime_today_str));


# pip install maya
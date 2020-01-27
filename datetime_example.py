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

# add some day in today's
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
hour_delta = datetime.timedelta(hours=10);
print(todayDT + hour_delta)


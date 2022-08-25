from  datetime import date,timedelta
def all_sundays(year):
    dt = date(year, 1, 1)
    print("-------------------")

    dt += timedelta(days=6 - dt.weekday())
    while dt.year == year:
        yield dt
        dt += timedelta(days=7)

for s in all_sundays(2020):
    print(s)

print("------------------------------------")

from datetime import date
a = date(2000,2,28)
b = date(2001,2,28)
print(b-a)

print("-----------------")

#specific monthille days check cheyyan
from  calendar import monthrange
year = 2016
month = 2
print(monthrange(year, month)[1])
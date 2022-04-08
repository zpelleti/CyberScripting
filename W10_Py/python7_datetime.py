
# info on timedelta: https://docs.python.org/3/library/datetime.html

from datetime import date 
from datetime import time
from datetime import datetime
from datetime import timedelta      # use datetime.timedelta

now = datetime.now()                # current date/time


print (now.strftime("Current year: %Y"))    # %Y = year 
print (now.strftime("%A %d th %B, %y"))      # week  day month (letter) year(abbreviated) 
print (now.strftime("%a %D"))                # caps D = numeric format full date
                                             # lower caps = abbreviate

print (now.strftime("Local date: %x or %D"))
print (now.strftime("Local time: %X"))
print (now.strftime("Local date+time: %c"))


print("Now: ",(now))

### Time Formatting ###
print("### Time Formatting ###")

print (now.strftime("Current time: %I:%M:%S %p"))    # 12hr format-> hr:min:sec:am/pm
print (now.strftime("Current time: %H:%M"))          # 24 hr format

print("====================")

today = date.today()
print("Today: " , today)
print("Today: " , today.year,today.month,today.day)   # samesies


print ("Weekday#: ", today.weekday())   # Mon = 0, Sun = 6 
days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
print("Weekday: " ,days[today.weekday()])        

print("=========Timedelta===========")

print (timedelta(days=365, hours = 5, minutes = 1)) # format time and days/year 

print  ("One year ago: " + str(now - timedelta(days=365)))
print  ("One year plus: " + str(now + timedelta(days=365)))

print ("Add two weeks and three days: " + str(now + timedelta(weeks = 2, days = 3)))

time = datetime.now() - timedelta(weeks = 1)
string = time.strftime("%A %B %d, %Y")    # %A = weekday
                                          # %B = month
                                          # %d = day, decimal num
                                          # %Y = year, decimal num
print("Full Date a week ago: (now - weeks = 1) " + string)

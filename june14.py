#modules
#timemodule
import time
print(time.time())
print(time.gmtime(200000))

print(time.asctime())
print(time.asctime(time.gmtime()))

print(time.ctime()) #perform same fn as asctime
print(time.ctime(24000)) #accepts only seconds

print(time.localtime()) #to knw local time
print(time.asctime(time.localtime())) #pass local time in asc time to get current time

#datemodule
import datetime
from datetime import date
#using MINYEAR to represent minimum representable year
print("minimum representable year is:",end="")
print(datetime.MINYEAR)

print("maximum representable year is:",end="")
print(datetime.MAXYEAR)

print("the date is:",end="")
print(date.today())

print(date.fromtimestamp(24356))#usimg fromtimestamp() to calculate date

print(date.min)#minimumdate
print(date.max)#maximumdate

#mathmodule
import math

print(math.factorial(4))#to get factorial

#osmodule
import os
print(os.name)#tell the name of ur os
print(os.getcwd())
print(os.environ)
import datetime
from datetime import date
#ques1
#time()– This function is used to count the number of seconds elapsed since the epoch.

#ques2
import time
print()
print(time.asctime(time.localtime()))

#ques3
#method1
a='14-6-2018'
date=datetime.datetime.strptime(a,"%d-%m-%Y")
print(date.month)
#method2
d=datetime.date.today()
print(d.month)

#ques4

import calendar
my_date = date.today()
z=calendar.day_name[my_date.weekday()]
print(z)

#ques5
b='11/01/2021'
d=datetime.datetime.strptime(b,"%d/%m/%Y")
print(d.day)

#ques6
print(time.localtime()) #to knw local time
print(time.asctime(time.localtime())) #pass local time in asc time to get current time

#ques7
import math
x=int(input("enter no.:"))
c=math.factorial(x)
print(c)

#ques8
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
m=math.gcd(a,b)
print(m)

#ques9
import os
#1
print(os.getcwd())
#2
print(os.environ)
#regular expression
#1.finadall
#2.search 3.compile
import re
str='''Abc is 18 yr old
Xyz is 20 yr old
Mno is 21 yr  old
'''
name=re.findall("[A-Za-z*]",str)
print(name)
age=re.findall("\d{1,3}",str)
print(age)
a=re.findall("\D",str)#\D=^\d
print(a)

nameage='''
Abc is 22 and Ghi is 32
Def is 43 and Ric is 21
'''
strr='sat cat mat rat'
regex=re.compile("[c-m]at")
strr=regex.sub("st",strr)
print(strr)

email="xyz@gmail.com acv.com vsd@gmail"
match=re.findall("[\w.%_+-]{1,20}[@][\w]{1,20}[.][A-Za-z]{1,3}",email)
print(match)

no="+91-885508-2050"
mat=re.findall("[+][\d]{1,4}[-][\d]{6,10}[-][\d]{4,10}",no)
print(mat)
#.group

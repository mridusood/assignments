#ques1
'''name of exception:ZeroDivisionException'''
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("no. divide by zero")

#ques2
'''IndexError'''
try:
    l= [1, 2, 3]
    print(l[3])
except IndexError:
    print("enter no. from list")

#ques3
'''An exception'''

#ques4
'''-5
a/b result in 0
'''

#ques5
#1
try:
    import richa
    print("richa")
except ImportError:
    print("there is an import error")
#2
try:
    a=int(input("enter no."))
    print(a)
except ValueError:
    print("please enter only integer")
#3
try:
    a=[1,2,3]
    print(a[4])
except IndexError:
    print("enter no. from list")

#ques6
class AgeTooSmallError(Exception):
    pass
a=True
while(a):

    try:
        age=int(input("enter age "))
        if (age < 18):
            raise AgeTooSmallError
        else:
            a=False
            print("entered age is %d"%age)
    except AgeTooSmallError:
        print("entered age is less than 18")

try:
    a=int(input("enter no."))
    print(a)
    b=10/a
   # print(b)
except ValueError:
    print("please enter only integer")
except ZeroDivisionError:
    print("no. divided by zero")
#except(valueerror,zerodivisionerror):
else:
    print(b)
finally:
    print("i will execute whether error occur or not")

try:
    a=[1,2,3]
    print(a[4])
except IndexError:
    print("enter no. from list")

try:
    import richa
    print("richa")
except ImportError:
    print("there is an import error")

class AddError(Exception):
    pass

try:
     a=int(input("enter 1 no."))
     b=int(input("enter 2 no."))
     c=a+b
     print(c)
     if(c<10):
         raise AddError
except AddError:
    print("sum should be greater than 10")



#except nameerror as argument e
#print(e)




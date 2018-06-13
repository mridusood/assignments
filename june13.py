#require keywords
#def add(a,b):
 #   return a+b
#print(add(2,3))

#def hello():
 #   print("hello")
  #  return 0
#hello()

#a=2
#b=3
#def add(a,b):
 #   return a+b
#print(add(a,b))

#default keywords
#def add(a,b=1):
 #   return a+b
#print(add(2))

#def add (c,d):
 #   return c+d
#print(add(d=2,c=5))

#a=2
#def add (a):
 #   a=3
  #  print(a)
#add(a)

def add (a,b):
    return a+b
def subtract(a,b):
    sub=a-b
    return sub
ch=int(input("enter choice"))
c=int(input("enter a"))
d=int(input("enter b"))
if ch==1:
    print(add(a,b))

if ch==2:
    print(subtract(a,b))


def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
x=int(input("enter limit"))
print(factorial(x))

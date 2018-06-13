#ques1
ar=1
r=int(input("enter radius"))
def area(r):
    ar=22.7*r*r
    return ar
print(area(r))

#ques2
i=0
sum=0
def perfect():
    for i in range(1,1000):
        sum=0
        for j in range(1,i):
            if(i%j==0):
                sum=sum+j;

        if sum==i:
            print("%d"%(i))
    return 0
print("The perfect no. are:")
perfect()

#ques3
def times_tables(n=12, t=0):
    if t == 11:
        return
    print(str(n) + " x " + str(t) + " = " + str(n*t))
    times_tables(n, t+1)
times_tables()

#ques4
result=1
a=int(input("Enter no."))
b=int(input("Enter power"))

def power(a,b):
    if b!=0:
        return (a*power(a,b-1))
    else:
        return 1
result=power(a,b)
print("result is: =%d"%(result))


#ques5
x=int(input("enter number"))
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
dict={'number':x,'factorial':factorial(x)}
print(factorial(x))
print(dict)



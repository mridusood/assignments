#ques1

y=int(input("enter year"))
if(y%4==0):
    print("year is leap year")


else:
    print("year is not leap year")

#ques2

length=int(input("length:"))
breadth=int(input("breadth:"))
if(length==breadth):
    print("it is square")

else:
    print("it is rectangle")

 #ques3

a=int(input("enter age of a:"))
b=int(input("enter age of b:"))
c=int(input("enter age of c:"))

if(a>b and a>c):
    print("a is older")

if(b>a and b>c):
        print("b is oldest")

if(c>a and c>b):
            print("c is oldest")

elif(a<b and a<c):
    print("a is youngest")
elif(b<a and b<c):
    print("b is youngest")
elif(c<a and c<b):
    print("c is youngest")

else:
    print("all ages are equal")


#ques4
z=int(input("enter points:"))
if z>1 and z<=50 :
    print("Sorry!No prize this time")
if z>50 and z<=150 :
    print("Congratulations! you won a wooden dog!")
if z>150 and z<=180 :
    print("Congratulations! you won a book!")
if z>180 and z<=200 :
    print("Congratulations! you won a chocolates!")


#ques5
q=int(input("quantity:"))
if(q*100>1000):
    print("cost is:%.2f"% ( q*100-0.10*q*100))

else:
    print("cost is:"+ q*100)

#ques1
i=0
while(i<10):
    num=input("enter your no.:")
    print("entered num is" + num)
    i=i+1

#ques2
#while(True):
 #   print("infinite")

#ques3
i=0
a=[]
while(i<5):
    num=int(input("enter the element"))
    a.insert(i,num)
    i+=1

i=0
print(a)
while(i<5):
    print("square of elements= %s"%(a[i]*a[i]))
    i=i+1

#ques4
x=['mridu',30,22.5,1,'hello','hi']
i=0
l_1=[]
l_2=[]
s_t=[]
y=[]

l_1 = [y for y in x if type(y) == int]
l_2 = [y for y in x if type(y) == float]
s_t = [y for y in x if type(y) == str]

print("Integer list")
print(l_1)
print("Float list")
print(l_2)
print("String list")
print(s_t)


#ques5

odd=[]
even=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)

#ques6
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()

#ques7
d={'name':'MRIDU','age':20,'city':'KAPURTHALA','University':'DAV uni'}
for i in d:
    print(d[i])
print(dict.keys(d))
print(dict.items(d))

#ques8
a=[]
i=0
while i<=4:
   num=int(input("ENTER THE VALUE"))
   a.append(num)
   i+=1

print(a)
i=0

s=int(input("ENTER THE VALUE YOU WANT TO DELETE"))
if s in a:
    a.remove(s)
    print("ElEMENT REMOVED!")
else:
    print("ELEMENT NOT FOUND")
print(a)




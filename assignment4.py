#assignment 4
#ques1
s=(1,3,8.8,"hello")
print(s)
t=len(s)
print(t)

#ques2
t=(8,1,0,45)
print(max(t))
print(min(t))

#ques3
t=(2*4*1)
print(t)

#SETS
#ques1
a1=input("enter the set 1")
a2=input("enter the set 1")

b1=input("enetr the set 2")
b2=input("enter the set 2")

set1=set([a1,a2])
set2=set([b1,b2])
#1
g=set1-set2
print(g)

#2
ans1=set1<=set2
ans2=set1>=set2
print(ans1)
print(ans2)

#3
set3=set1&set2
print(set3)

#dictionary
#ques1
name=input("enter the name")

marks=input("enetr the marks")
d={'name':name, 'marks':marks}
print(d)

#ques2
#ques3
word="MISSISSIPPI"
m=word.count("M")
i=word.count("I")
s=word.count("S")
p=word.count("P")

d={"no. of M":m , "no. of I": i, "no. of S":s , "no. of P":p }
print(d)


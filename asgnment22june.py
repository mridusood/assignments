#ques1

f=open("text.txt",encoding="utf-8")
n=int(input("enter number of last lines you want to be printed"))
l=f.readlines()
l.reverse()
print(l[:n])


#Ques2
word = input("Enter word to be searched:")
k = 0
f=open("text.txt",encoding="utf-8")
for line in f:
    words = line.split()
    for i in words:
        if (i == word):
            k = k + 1
print("Occurrences of the word:")
print(k)


#Ques3
f=open("text.txt",encoding="utf-8")
a=open("file.txt",'r+')
f1=f.readlines()
for i in f1:
    a.write(i)
print(a.read())


#ques4
x=open("demo1.txt",encoding="utf-8")
y=open("demo2.txt",encoding="utf-8")
z=open("add.txt",'r+')
x1=x.readlines()
y1=y.readlines()
for i,j in zip(x1,y1):
    z.write(i+j)
    print(i+j)

#ques5
print("")
i=0
randomlist=[]
import random
for i in range(0,10):
    randomlist.append(random.randrange(0,100))
    randomlist[i]=str(randomlist[i])
print(randomlist)
print(sorted(randomlist))
f1=open("demo3.txt","r+")
f1.writelines(randomlist)
print(f1.readline())
print("read")

f1.close()
f1=open("sorted.txt","r+")
f1.writelines(sorted(randomlist))
print(f1.readline())
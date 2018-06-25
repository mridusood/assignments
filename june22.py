#file_handling
#f=open("test.txt","r") #calling init method
#print(f)
#print(f.read())
#print(f.readline())
#print(f.readline())
#print(f.readlines())
#print(f.close())

#f=open("test.txt","r+")
#l=["hello\n","welcome to acadview\n"]
#f.writelines(l)

with open("test.txt","r+") as f:
    a=["richa\n","sood\n"]
    f.writelines(a)
    print(f.read(4))
    print(f.tell())
    print(f.seek(5,0))
    print(f.tell())
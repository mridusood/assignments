#ques1
import threading
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        time.sleep(5)
        print("hello",self.h)

thread1=mythread('world')
thread1.start()

#ques2
class mythread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):

        print(self.h)
for i in range(11):
    thread1=mythread(i)
    thread1.start()
    time.sleep(1)

#ques3
class mythread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        n=2
        l=(1,2,3,4,5)
        for i in l:
            time.sleep(n)
            print("element is %d"%i)
            n=n+2


thread = mythread("")
thread.start()
thread.join()

#ques4
import math
a=int(input("enter the no:"))
class f(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        global result
        temp = math.factorial(self.num)
        print (" the factorial of %d is %d" %(self.num,temp))
        result += temp

result = 0
threads = f(a)
f(a).start()
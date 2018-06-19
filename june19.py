#threading
import threading
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):

        print("value send:",self.h)

thread1=mythread(1)
thread1.start()
time.sleep(5)
thread2=mythread(2)
thread2.start()

class mythread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        #time.sleep(1)
        print("no. is:", self.h)
for i in range(10):
    thread1=mythread(i)
    thread1.start()

print("active threads are",threading.activeCount())

class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        print("hello i m in run",self.h)
thread1=mythread("from thread 1")
thread1.start()
thread1.join()
thread2=mythread("from thread 2")
thread2.start()
thread2.join()
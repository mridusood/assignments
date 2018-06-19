from threading import Thread
import time
def sleepMe(i):
    print("Thread %i going to sleep for 5 sec"%i)
    time.sleep(5)
    print("thread %i is awake now."%i)
for i in range(10):
    th=Thread()

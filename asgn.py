import numpy as np
import math

#Ques1
x=np.random.random((10,1))
print (x)
m=x.mean()
print("mean is "+str(m))

#Ques2
y=np.random.random((20,1))
print(y)
a=y.var()
print("variance is "+str(a))
b=y.std()
print("standard deviaation is "+str(b))

#Ques3
s=np.random.random((10,20))
t=np.random.random((20,25))
#a.dtype=np.float64
#b.dtype=np.float64
#print(a*b)
c=s@t
print(c)
d=np.sum(c)
print("sum of all elements of new matrix is "+str(d))
#ques4

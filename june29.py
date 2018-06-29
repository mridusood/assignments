import numpy as np
#a=np.array([1,2,3])
#print(type(a))
#print(a.shape)
#print(a[0],a[1],a[2])
#a[0]=5
#print(a)
#b=np.array([[1,2,3],[4,5,6]])
#print(b.shape)
#print(b[0,0],b[0,1],b[1,0])
a=np.zeros((2,2))
print(a)
b=np.ones((1,2))
print(b)
c=np.full((2,2),7)
print(c)
d=np.eye(2)#identity matrix
print(d)
e=np.random.random((2,2))#give the result between 0 and 1
print(e)

z=np.arange(15).reshape(3,5)
print(z)

y=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
row_r1=y[1 ,:]
print(row_r1)
row_2=y[1:2,:]
print(row_2)

l=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(l)
m=np.array([0,2,0,1])
print(l[np.arange(4),m])

l[np.arange(4),m] +=10
print(l)

bool_idx=(l>2)
print(bool_idx)
print(l[bool_idx])

v=np.array([[1,2],[3,4]])
print(np.sum(v))
print(np.sum(v,axis=0))
print(np.sum(v,axis=1))
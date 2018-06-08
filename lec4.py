
#tuple
a=[1,2,3]
b=tuple(a)
print(b)
d=[3,4,5]
c=str(d)
print(c)

t=(1,2,3,4,5)
print(max(t))
print(min(t))

s1=set([1,2,3])
s2=set([3,4,5])
s3=s1|s2
print(s3)
s4=s1&s2
print(s4)
s2.add(2)
print(s2)
s2.remove(3)
print(s2)
s2.discard(2)
print(s2)
s2.pop()
print(s2)

g={1,2,3,4,5}
h={2,3,4}
i=g<=h
print(i)
j=g>=h
print(j)

#dictionary
d={'name':'abc', 'sciencemarks':30,'engmarks':45, 'mathmakrs':93}
print(d)
print(d["engmarks"])
d['engmarks']=98
print(d)

#d.clear()
print(d)

del d['engmarks']
print(d)

del d



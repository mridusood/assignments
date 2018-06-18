#ques1
typ=input("type of animal is:")
legs=int(input("enter the no. of legs:"))
class Animal:
    def animal_attribute(self,typ,legs):
      print("type of animal is:"+ typ)
      print("no. of legs: %d"%(legs))
class Tiger(Animal):
    def animal_attribute(self,typ,legs):
        typ=input("the animal is tiger")
        legs=(input(4))
x=Animal()
y=Tiger()
x.animal_attribute(typ,legs)
y.animal_attribute(typ,legs)

#ques2
print("the output is: AB and AB")

#ques3
class Cop:
    def __init__(self,name,age,wrkexp,desg):
        self.name=name
        self.age=age
        self.wrkexp=wrkexp
        self.desg=desg



    def add(cls):
        cls.name = input("enter the name of cop:" )
        cls.age = int(input("Enter the age of cop:"))
        cls.workexp = int(input("Enter the work experience of cop:"))
        cls.desg = input("Enter the designation:")
        return Cop(cls.name, cls.age, cls.workexp, cls.desg)

    def display(cls):
        print("")
        print("Details are:")
        print("Name: " + cls.name)
        print("Age: %d" % cls.age)
        print("Work experience %d" % cls.workexp)
        print("Designation" + cls.desg)

    def update(self):
        print("Update details")
        self.add()
        self.display()


class Mission(Cop):
    def __init__(self, mission_details):
        self.md = mission_details

    def add_mission_details(self):
        self.md = input("Enter mission details: ")
        print("")
        self.display()
        print("Mission details:" + self.md)


xyz = Mission("")
obj1 =Cop("",0,0,"")
obj1.add()
obj1.display()
ch = input("DO YOU WANT TO UPDATE THE DETAILS?(Y/N)")
if ch == 'y' or ch == 'Y':
    obj1.update()
ch = input("DO YOU WANT TO RUN MISSION CLASS?(Y/N)")
if ch == 'y' or ch == 'Y':
    xyz.add_mission_details()


#ques4
a=float(input("enter length:"))
b=float(input("enter breadth:"))
class Shape:
    def __init(self,a,b):
        self.l=a
        self.b=b
    def area(self):
        print("area is %d"%(self.l*self.b))

class Rectangle(Shape):
    def area(self,a,b):
        return a*b

class Square(Shape):
    def area(self,a):
        return a*a

obj=Shape()
obj1=Rectangle()
obj2=Square()
print("area of rectangle is: %d"%(obj1.area(a,b)))
print("area of square is : %d"%(obj2.area(a)))

#ques1
r=int(input("enter the radius:"))
class Circle:
     def getArea(self,r):
        ar=3.14*r*r
        print("area of the circle is: %.2f" %(ar))
        return 0


     def getCircumfrence(self,r):
        cir=2*3.14*r
        print("circumfrence of the circle is: %.2f"%(cir))
        return 0
x=Circle()
x.getArea(r)
x.getCircumfrence(r)

#ques2
name=input("enter your name:")
rn=int(input("enter your roll. no:"))
class Student:
    def display(self,name,rn):
        print(name)
        print(r)
h=Student()
h.display(name,rn)

#ques3
fn=float(input("enter the farenhite:"))
cl=float(input("enter the celsius:"))
class Temperature:
    def convertFarenhite(self,cl):
        z=cl*9/5+32
        print("conversion of celsius to farenhite is: %.2f"%(z))

    def convertCelsius(self,fn):
        y=(fn-32)*1.8
        print("conversion of farenhite to celsius is:: %.2f"%(y))
s=Temperature()
s.convertFarenhite(cl)
s.convertCelsius(fn)

#ques4
name=input("enter the name of movie:")
art=input("enter the artist name:")
yr=int(input("enter the year of release:"))
rt=int(input("rate out of 5:"))
class MovieDetails:
    def displays(self,name,art,yr,rt):
        print("name of the movie:"+name)
        print("name of the artist:" +art)
        print("year of release is: %.2f"%(yr))
        print("rating is: %.2f"%(rt))

    def updatedetails(self,name,art,yr,rt):
     name = input("ENTER MOVIE NAME ")
     art = input("ENTER ARTIST NAME ")
     yr = input("ENTER YEAR OF RELEASE ")
     rt = int(input("ENTER RATINGS "))

    print("NEW MOVIE NAME " + name)
    print("NEW ARTIST NAME " + art)
    print("NEW YEAR OF RELEASE %.2f" % (yr))
    print("NEW RATINGS%d" % (rt))

print("movie details:")

t = MovieDetails()
t.displays(name, art, yr, rt)

ch3 =int(input("want to update details? (1/2)"))

if ch3==1:
    print("no updation")

elif ch3==2:
    print("updates details:")
    t.updatedetails(name, art, yr, rt)


#ques5

exp=0
sav=0
sal=0
class Expenditure:
    def displayresult(self, exp,sav):
        print("EXPENDITURE::%.2f"%(exp))
        print("SAVINGS::%.2f"%(sav))
        print("")
    def calculateresult(self, exp,sav):
        sal=exp+sav

    def displaysalary(self, sal):
        print("SALARY -->%.2f" % (sal))


exp = int(input("ENTER THE EXPENDITURE"))
sav = int(input("ENTER THE SAVINGS"))

zzz = Expenditure()
zzz.displayresult(exp,sav)
zzz.calculateresult(exp,sav)
zzz.displaysalary(sal)




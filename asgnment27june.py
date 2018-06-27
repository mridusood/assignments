import tkinter
#ques1
from tkinter import *
top=Tk()
a=Label(top,text='hello world')
a.pack()
btn=Button(top,text='exit',command=" ")
btn.pack()
top.mainloop()

#ques2
hi=tkinter.Tk()
def close():
    hi.destroy()
def write():
    print("hello world")
hi.title("MRIDU")
hi.geometry("500x500")
btn=tkinter.Button(hi,text="exit",command=close)
btn1=tkinter.Button(hi,text="click",command=write)

btn.pack()
btn1.pack()
btn1.place(x=90,y=90)
btn.place(x=50,y=50)
hi.mainloop()



#Ques3
from tkinter import *
test=Tk()
frame=Frame(test)
frame.pack()
lbl=Label(test,text='working with frames')
lbl.pack()
button1=Button(frame,text='exit',fg='blue')
button1.pack()
button2=Button(frame,text='change label',fg='red')
button2.pack()
mainloop()



#Ques4
from tkinter import *
master=Tk()
master.geometry("100x100")
Label(master,text='input').grid(row=0)
e1=Entry(master)
e1.grid(row=0,column=1)
mainloop()

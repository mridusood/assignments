import tkinter #import tkinter as tk
top=tkinter.Tk() #container's name is top
top.title("richa")
top.size()
top.geometry("400x400") #to adjust size of container
btn=tkinter.Button(top,text="hello there!",bg='red',command=" ")
#btn.pack()-it will automatically adjust button in any position
btn.place(x=50,y=50)


top.mainloop() #to get empty gui

from tkinter import *
master=Tk()
w=Canvas(master,width=40,height=60)
#w.pack()
#canvas_height=20
#canvas_width=200
#y=int(canvas_height/2)
#w.create_line(0,y,canvas_width,y)
#w.create_oval(0,y,canvas_width,y)
var1=IntVar()
Checkbutton(master,text='male',variable=var1).grid(row=0 ,column=1)
var2=IntVar()
Checkbutton(master,text='female',variable=var2).grid(row=1, column=2)

Label(master,text='First Name').grid(row=2)
Label(master,text='Last Name').grid(row=3)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=2,column=3)
e2.grid(row=3,column=3)
w.mainloop()
root=Tk()
frame=Frame(root,bg='black')
frame.pack()
redbutton=Button(frame,text='Red',fg='yellow',bg='brown')
redbutton.pack()
greenbutton=Button(frame,text='green',fg='pink',bg='brown')
greenbutton.pack()
root.mainloop()

a=Tk()
tb=Listbox(a)
tb.insert(1,'jai')
tb.insert(2,'mata')
tb.insert(3,'di')
tb.pack()
a.mainloop()
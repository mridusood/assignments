import tkinter
from tkinter.filedialog import askopenfile
from tkinter import *
from tkinter import messagebox
def cmd1():
   #print("new is click:")
   #lb1.config(text="acadview")
   messagebox.showinfo("say hello","hello world")
   messagebox.showwarning("error","error occured")
def cmd2():
     a=askopenfile()
def calculate():
    a=w1.get()
    b=w2.get()
    messagebox.showerror('info',a and b)
root=Tk()
menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=cmd1)
filemenu.add_command(label='Open',command=cmd2)
filemenu.add_command(label='scale',command=calculate)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)

lb1=Label(root,text='hello')
lb1.pack()


from tkinter import *
main=Tk()
ourMessage='This is our Message'
messageVar=Message(main,text=ourMessage)
messageVar.config(bg='grey')
messageVar.pack()
main.mainloop()
master=Tk()
w1=Scale(master,from_=0,to=44)
w1.pack()
w2=Scale(master,from_=0,to=200,orient=HORIZONTAL)
w2.pack()

master.mainloop()
mainloop()
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox

d={'a':'8872296040',
   'b':'1234567890',
   'c':'0987654321'}
master=Tk()
master.title("scroll bar")
master.geometry('50x50')
s=Scrollbar(master)
s.pack(side=RIGHT,fill=Y)
mylist=Listbox(master,yscrollcommand=s.set)
for i in d:
    mylist.insert(END,"name "+ str(i))
    mylist.insert(END,"phone "+str(d[i]))
mylist.pack( side = LEFT, fill = BOTH )
s.config( command = mylist.yview )
mainloop()

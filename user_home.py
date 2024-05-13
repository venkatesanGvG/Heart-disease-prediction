import os
from tkinter import *
from tkinter import messagebox
import pymysql
import sample_data
from sample_data import student
import os
def new_registration():
    root.destroy()
    import home



def new_registration1():
    root.destroy()
    import view_data
 

root = Tk()
w=780
h=500
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Heart Disease Predicion")
message = Label(root, text="Heart Disease Predicion",fg="#004080", width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=2, y=20)

message1 = Label(root, text="Dataset Input",height=1, font=('Helvetica', 20, 'bold'))
message1.place(x=320, y=170)
message1.bind('<Button-1>', lambda *_: new_registration())


message1 = Label(root, text="View Data",height=1, font=('Helvetica', 20, 'bold'))
message1.place(x=320, y=270)
message1.bind('<Button-1>', lambda *_: new_registration1())

root.mainloop()

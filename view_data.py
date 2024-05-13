import os
import shutil
import tkinter
from tkinter import *
from tkinter import ttk, messagebox

import pymysql

import sample_data


def view_details():
    def read_data_delete():
        a=txt91.get()
        sample_data.student.s_name=a
        to = pymysql.connect(host="localhost", user="root", password="", database="python_heart_disease_prediction")
        cursor=to.cursor()
        cursor.execute("DELETE from user_data where id='"+str(a)+"'")
        to.commit()
        messagebox.showinfo('Success',"Delete Successfully")
        read_data_set()
    def read_data_set_1():

        read_data_set()
    def read_data_set():
        def selectItem(a):
            curItem = tree.focus()
            data=(tree.item(curItem))
            data1=(data['values'])

            txt91.delete(0,END)
            txt91.insert(0,data1[0])
            sample_data.student.s_id=data1[0]

        to = pymysql.connect(host="localhost", user="root", password="", database="python_heart_disease_prediction")
        my_conn = to.cursor()

        my_conn.execute("SELECT * FROM  user_data  order by id DESC")
        i=0
        TableMargin = Frame(read_data_main, width=500)
        TableMargin.place(x=50, y=110,width=605, height=255)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("id","age","sex","chol","oldp","thala"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('id', text="id", anchor=W)
        tree.heading('age', text="age", anchor=W)
        tree.heading('sex', text="sex", anchor=W)
        tree.heading('chol', text="chol", anchor=W)
        tree.heading('oldp', text="oldp", anchor=W)
        tree.heading('thala', text="thala", anchor=W)
        tree.bind('<ButtonRelease-1>', selectItem)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=50)
        tree.column('#2', stretch=NO, minwidth=0, width=50)
        tree.column('#3', stretch=NO, minwidth=0, width=90)
        tree.column('#4', stretch=NO, minwidth=0, width=90)
        tree.column('#5', stretch=NO, minwidth=0, width=90)
        tree.pack()
        for  hr_addsalary  in my_conn:
            tree.insert("", 0, values=hr_addsalary)
        tree.pack()
############################################################






    # read_data_main =tkinter.Toplevel()
    read_data_main =Tk()
    w=750
    h=550
    ws = read_data_main.winfo_screenwidth()
    hs = read_data_main.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    read_data_main.geometry('%dx%d+%d+%d' % (w, h, x, y))

    read_data_main.title("Heart Disease Predicion")
    read_data_main.resizable(False, False)

########################################################### Element design

    message = Label(read_data_main, text="View Data", width=35,height=3, font=('times', 30, 'bold '))
    message.place(x=00, y=10)
    # txt9= Entry(read_data_main,width=15, font=('times', 15, ' bold '))
    # txt9.place(x=210,y=380)
    # resust_dataset = Button(read_data_main, text="Search",height=1,command=read_data_set_1,font=('times', 15, ' bold '))
    # resust_dataset.place(x=380, y=380)
    #

    txt91= Entry(read_data_main,width=15, font=('times', 15, ' bold '))
    txt91.place(x=210,y=420)


    resust_dataset = Button(read_data_main,width=13, text="Delete",height=1,command=read_data_delete,font=('times', 14, ' bold '))
    resust_dataset.place(x=210, y=490)

    read_data_set()
    resust_dataset.mainloop()


view_details()
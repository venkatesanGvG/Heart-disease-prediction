from tkinter import *
import os
# from tkFileDialog import askopenfilename
import csv
import sample_data
from tkinter import *
import tkinter.ttk as ttk
import csv
########################################################### function
def next_page():
    attribut_extraction_data_main.destroy()
    import random_forest
def read_data_set():
    root = Tk()
    root.title("Attribute Extraction")
    width = 550
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)


    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("age","sex", "cp", "trestbps", "chol","restecg","thalach","oldpeak"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('age', text="age", anchor=W)
    tree.heading('sex', text="sex", anchor=W)
    tree.heading('cp', text="cp", anchor=W)
    tree.heading('trestbps', text="trestbps", anchor=W)
    tree.heading('chol', text="chol", anchor=W)

    tree.heading('restecg', text="restecg", anchor=W)
    tree.heading('thalach', text="thalach", anchor=W)

    tree.heading('oldpeak', text="oldpeak", anchor=W)



    # tree.heading('EC1 Pre', text="EC1 Pre", anchor=W)
    # tree.heading('EC2 Post', text="EC2 Post", anchor=W)
    #
    # tree.heading('Ni1 Pre', text="Ni1 Pre", anchor=W)
    # tree.heading('Ni2 Post', text="Ni2 Post", anchor=W)
    #
    # tree.heading('Cu1 Pre', text="Cu1 Pre", anchor=W)
    # tree.heading('Cu2 Post', text="Cu2 Post", anchor=W)
    #
    # tree.heading('Mn1 Pre', text="Mn1 Pre", anchor=W)
    # tree.heading('Mn2 Post', text="Mn2 Post", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=200)
    tree.column('#5', stretch=NO, minwidth=0, width=200)
    tree.column('#6', stretch=NO, minwidth=0, width=200)
    tree.column('#7', stretch=NO, minwidth=0, width=200)
    # tree.column('#8', stretch=NO, minwidth=0, width=200)
    # tree.column('#9', stretch=NO, minwidth=0, width=0)
    # tree.column('#10', stretch=NO, minwidth=0, width=200)
    # tree.column('#11', stretch=NO, minwidth=0, width=200)
    # tree.column('#12', stretch=NO, minwidth=0, width=200)
    # tree.column('#13', stretch=NO, minwidth=0, width=200)
    # tree.column('#14', stretch=NO, minwidth=0, width=200)
    # tree.column('#15', stretch=NO, minwidth=0, width=200)
    # tree.column('#16', stretch=NO, minwidth=0, width=200)
    # tree.column('#17', stretch=NO, minwidth=0, width=200)

    tree.pack()
    ob=sample_data
    file="data_set/irrelevant.csv"
    with open(file) as f, open('data_set/attributes.csv', 'w') as csvfile:

        reader = csv.DictReader(f, delimiter=',')
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['age','sex', 'cp', 'trestbps', 'chol','restecg','thalach','oldpeak'])
        for row in reader:
            #print row
            t1 = row['age']
            t2 = row['sex']
            t3 = row['cp']
            t4 = row['trestbps']
            t5 = row['chol']
            t6 = row['restecg']
            t7 = row['thalach']
            t8 = row['oldpeak']


            tree.insert("", 0, values=(t1,t2,t3,t4,t5,t7,t8))
            filewriter.writerow([t1,t2,t3,t4,t5,t7,t8])

############################################################
attribut_extraction_data_main = Tk()
w=750
h=550
ws = attribut_extraction_data_main.winfo_screenwidth()
hs = attribut_extraction_data_main.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
attribut_extraction_data_main.geometry('%dx%d+%d+%d' % (w, h, x, y))
attribut_extraction_data_main.title("Cardio Vascular Disease")

########################################################### Element design


message = Label(attribut_extraction_data_main, text="Cardio Vascular Disease",fg="#003366", width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=10)

compare_dataset = Button(attribut_extraction_data_main, text="Attribute Extraction",width=15,command=read_data_set  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=150, y=400)
resust_dataset = Button(attribut_extraction_data_main,command=next_page , text="Next",width=15  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=400)

attribut_extraction_data_main.mainloop()

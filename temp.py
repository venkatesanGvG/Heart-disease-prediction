
import numpy as np
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt
import pandas as pd
import pymysql
from sklearn.ensemble import RandomForestRegressor
from tkinter import messagebox
from tkinter import *
import tkinter.ttk as ttk
import csv
########################################################### function

from sample_data import student


def result():
    dd=0
    age=txt.get()
    sex=jj.get()
    chol=kk.get()
    oldp=pp.get()
    thala=ww.get()
    if age == '':
        messagebox.showwarning("Enter Age","Enter Age")
    elif sex == '':
        messagebox.showwarning("Enter Sex","Enter Sex")
    elif chol == '':
        messagebox.showwarning("Enter Chol","Enter Chol")
    elif oldp == '':
        messagebox.showwarning("Enter Oldp","Enter Oldp")
    elif thala == '':
        messagebox.showwarning("Enter thala","Enter thala")
    else:
        to = pymysql.connect(host="localhost", user="root", password="", database="python_heart_disease_prediction")
        cursor = to.cursor()
        cursor.execute("Select max(id)+1 From user_data")
        maxid = cursor.fetchone()[0]
        if maxid is None:
            maxid = 1
        cursor = to.cursor()
        sql = "insert into user_data values('" + str(maxid) + "','" + age + "','" + sex + "','" +chol + "','" +oldp + "','" + thala + "','0','0')"
        cursor.execute(sql)
        to.commit()
        if(int(chol)<200):
            print("")
            messagebox.showinfo("Result","Desirable")
        elif(int(chol)<240):
            print( "")
            messagebox.showinfo("Result","Border Line")
        else:
            print( "")
            messagebox.showinfo("Result","High")






def read_data_set():
    root = Tk()
    root.title("Random forest")
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
    tree = ttk.Treeview(TableMargin, columns=("age", "chol"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('age', text="age", anchor=W)
    tree.heading('chol', text="chol", anchor=W)


    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)


    tree.pack()
    file="data_set/attributes.csv"
    obj=student
    with open(file) as f, open('data_set/random_forest.csv', 'wb') as csvfile:

        reader = csv.DictReader(f, delimiter=',')
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['age','chol'])
        for row in reader:
            #print row
            t1 = row['age']
            t2 = row['chol']

            a=float(t2)


            tree.insert("", 0, values=(t1,a))
            filewriter.writerow([t1,a])
            #print c

            if(a<200):
                obj.acid.append(a)
                obj.acid1.append(t1)
                #print "acid" decirable
            elif(a<240):
                obj.neutral.append(a)
                obj.neutral1.append(t1)
                #print "neutral" border line
            else:
                obj.base.append(a)
                obj.base1.append(t1)
                #print "base" high

    data = pd.read_csv('data_set/random_forest.csv')
    #print(data)
    x = data.iloc[:, 1:2].values
    # print(x)
    y = data.iloc[:, 1].values
    regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
    regressor.fit(x, y)
    X_grid = np.arange(min(x), max(x), 0.01)
    X_grid = X_grid.reshape((len(X_grid), 1))
    plt.scatter(x, y, color = 'blue')
    plt.plot(X_grid, regressor.predict(X_grid),color = 'green')
    plt.title('Random Forest')
    plt.xlabel('Position level')
    plt.ylabel('Values')
    plt.show()
    #print obj.acid.__len__()




############################################################
random_forest_data_main = Tk()
w=750
h=550
ws = random_forest_data_main.winfo_screenwidth()
hs = random_forest_data_main.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
random_forest_data_main.geometry('%dx%d+%d+%d' % (w, h, x, y))
random_forest_data_main.title("Cardio Vascular Disease")

########################################################### Element design


message = Label(random_forest_data_main, text="Cardio Vascular Disease",fg="#003366", width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=10)


r=Label(random_forest_data_main,text="AGE",fg="red",font=("Arial",15)).place (x=230,y=150)
txt = Entry(random_forest_data_main,width=20,font=("Arial",18))
txt.place(x=350,y=150)
#txt.insert(0,"oppo a7")


i=Label(random_forest_data_main,text="SEX",fg="red",font=("Arial",15)).place (x=230,y=200)
jj=Entry(random_forest_data_main,width=20,font=("Arial",18))
jj.place(x=350,y=200)

k=Label(random_forest_data_main,text="Chol",fg="red",font=("Arial",15)).place (x=230,y=250)
kk=Entry(random_forest_data_main,width=20,font=("Arial",18))
kk.place(x=350,y=250)

p=Label(random_forest_data_main,text="Oldpeak",fg="red",font=("Arial",15)).place (x=230,y=300)
pp=Entry(random_forest_data_main,width=20,font=("Arial",18))
pp.place(x=350,y=300)

w=Label(random_forest_data_main,text="Thalach",fg="red",font=("Arial",15)).place (x=230,y=350)
ww=Entry(random_forest_data_main,width=20,font=("Arial",18))
ww.place(x=350,y=350)




resust_dataset = Button(random_forest_data_main,command=result , text=" Result",width=20  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=350, y=400)


random_forest_data_main.mainloop()

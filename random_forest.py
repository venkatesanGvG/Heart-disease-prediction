import numpy as np
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

from tkinter import *
import tkinter.ttk as ttk
import csv
########################################################### function

from sample_data import student

def nextpage():
    random_forest_data_main.destroy()
    import temp

def result():
    o1=student
    a1=o1.acid.__len__()
    a2=o1.neutral.__len__()
    a3=o1.base.__len__()
    print(a1,a2,a3)
    height1 = [a1, a2, a3]
    bars1 = ('Desirable', 'Border_line', 'High')
    y_pos1 = np.arange(len(bars1))
    plt.bar(y_pos1, height1, color=(0.9, 0.3, 0.8, 0.8))
    plt.xticks(y_pos1, bars1)
    plt.show()






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
    with open(file) as f, open('data_set/random_forest.csv', 'w') as csvfile:

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

compare_dataset = Button(random_forest_data_main, text="Random Forest",width=15,command=read_data_set  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=150, y=400)

resust_dataset = Button(random_forest_data_main,command=result , text=" Result",width=15  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=400)



resust_dataset = Button(random_forest_data_main ,command=nextpage , text="Next",width=15  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=450)

random_forest_data_main.mainloop()

import os
from tkinter import *
from tkinter import messagebox
import pymysql
import sample_data
from sample_data import student
import os
def new_registration():
    new_user = Tk()
    w = 400
    h = 550
    ws = new_user.winfo_screenwidth()
    hs = new_user.winfo_screenheight()
    x = (ws / 3) - (w / 3)
    y = (hs / 2) - (h / 2)
    new_user.geometry('%dx%d+%d+%d' % (750, 550, x, y))
    message = Label(new_user, text="NEW USER", fg="#E99F0A", height=1,
                    font=('Helvetica', 25, 'bold'))
    message.place(x=290, y=10)
    label = Label(new_user, text='NAME', fg=sample_data.student.text_color,
                  font=('times', 15, 'bold '))
    label.place(x=220, y=90)
    label = Label(new_user, text='FATHER NAME', fg=sample_data.student.text_color,
                  font=('times', 15, 'bold '))
    label.place(x=220, y=130)
    label = Label(new_user, text='CONTACT', fg=sample_data.student.text_color,
                  font=('times', 15, 'bold '))
    label.place(x=220, y=170)
    label = Label(new_user, text='EMAIL', fg=sample_data.student.text_color,
                  font=('times', 15, 'bold '))
    label.place(x=220, y=210)
    label = Label(new_user, text='ADDRESS', fg=sample_data.student.text_color,
                  font=('times', 15, 'bold '))
    label.place(x=220, y=250)
    label = Label(new_user, text='PINCODE', fg=sample_data.student.text_color,
                  font=('times', 15, 'bold '))
    label.place(x=220, y=290)
    label = Label(new_user, text='USERNAME', fg=sample_data.student.text_color,
                  font=('times', 15, 'bold '))
    label.place(x=220, y=330)
    label = Label(new_user, text='PASSWORD', fg=sample_data.student.text_color,
                  font=('times', 15, 'bold '))
    label.place(x=220, y=370)

    txt = Entry(new_user, width=15, font=('times', 15, ' bold '))
    txt.place(x=370, y=90)

    txt1 = Entry(new_user, width=15, font=('times', 15, ' bold '))
    txt1.place(x=370, y=130)

    txt2 = Entry(new_user, width=15, font=('times', 15, ' bold '))
    txt2.place(x=370, y=170)

    txt3 = Entry(new_user, width=15, font=('times', 15, ' bold '))
    txt3.place(x=370, y=210)

    txt4 = Entry(new_user, width=15, font=('times', 15, ' bold '))
    txt4.place(x=370, y=250)

    txt5 = Entry(new_user, width=15, font=('times', 15, ' bold '))
    txt5.place(x=370, y=290)

    txt6 = Entry(new_user, width=15, font=('times', 15, ' bold '))
    txt6.place(x=370, y=330)

    txt7 = Entry(new_user, show='*', width=15, font=('times', 15, ' bold '))
    txt7.place(x=370, y=370)


    def data():
        to = pymysql.connect(host="localhost", user="root", password="", database="python_heart_disease_prediction")
        cursor = to.cursor()
        a = txt.get()
        b = txt1.get()
        c = txt2.get()
        d = txt3.get()
        e = txt4.get()
        f = txt5.get()
        g = txt6.get()
        h = txt7.get()
        contact_length = len(c)
        contact_number = c.isdigit()

        pincode_ver = f.isdigit()
        pincode_len = len(f)
        if (a == ""):
            messagebox.showinfo('Alert', "Enter Name")
        elif (b == ""):
            messagebox.showinfo('Alert', "Enter Father Name")
        elif (c == ""):
            messagebox.showinfo('Alert', "Enter Contact")
        elif (d == ""):
            messagebox.showinfo('Alert', "Enter Email")
        elif (e == ""):
            messagebox.showinfo('Alert', "Enter Address")
        elif (f == ""):
            messagebox.showinfo('Alert', "Enter Pincode")
        elif (pincode_len != 6):
            messagebox.showinfo('Invalid', "Enter the 6 Digit Pincode")
        elif (pincode_ver == False):
            messagebox.showinfo('Invalid', "Enter the Valid Pincode No")
        elif (g == ""):
            messagebox.showinfo('Alert', "Enter Username")
        elif (h == ""):
            messagebox.showinfo('Alert', "Enter Password")
        elif (contact_length != 10):
            messagebox.showinfo('Invalid', "Enter the 10 Digit Mobile No")
        elif (contact_number == False):
            messagebox.showinfo('Invalid', "Enter the Valid Mobile No")

        else:
            cursor.execute("Select max(id)+1 From user_details")
            maxid = cursor.fetchone()[0]
            if maxid is None:
                maxid = 1
            cursor = to.cursor()
            sql = "insert into user_details values('" + str(
                maxid) + "','" + a + "','" + b + "','" + c + "','" + d + "','" + e + "','" + f + "','" + g + "','" + h + "','0','0')"
            try:
                cursor.execute(sql)
                to.commit()
                messagebox.showinfo('Success', "Registered Successfully")
                root.attributes("-topmost", True)
                root.attributes("-topmost", False)
                new_user.destroy()
            except:
                messagebox.showinfo('Failed', "Registration Failed")

    button = Button(new_user, text='Register', width=10, font=('times', 15, ' bold '), command=data)
    button.place(x=340, y=420)



def del_sc1():
    sc1.destroy()
def err_screen():
    global sc1
    sc1 = Tk()
    sc1.geometry('200x80')
    sc1.title('Warning!!')
    sc1.configure(background='snow')
    Label(sc1,text='Enrollment & Name required!!!',fg='#f5427e',bg='white',font=('times', 16, ' bold ')).pack()
    Button(sc1,text='OK',command=del_sc1,fg="black"  ,bg="#42bcf5"  ,width=9  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold ')).place(x=90,y= 50)
def clear():
    txt.delete(first=0, last=22)

def clear1():
    txt2.delete(first=0, last=22)

def training():
    a=txt.get()
    b=txt2.get()
    if (a==""):
        messagebox.showinfo(title="Alert", message="Enter Your email")
    elif(b==""):
        messagebox.showinfo(title="Alert", message="Enter Password")
    else:
        sql = "Select * from user_details where email='" + a + "' and password='" + b + "'"
        try:
            to = pymysql.connect(host="localhost", user="root", password="", database="python_heart_disease_prediction")
            cursor = to.cursor()

            cursor.execute(sql)
            myresult = cursor.fetchall()
            if (myresult):
                messagebox.showinfo('Alert', 'Success')
                sample_data.student.name = a
                root.destroy()
                import user_home
            else:
                msg = messagebox.showinfo('Failed', "Log In Failed")
        except:
            print(sys.exc_info()[0])
            msg = messagebox.showinfo('Failed', "Contact To Admin")



def testing():
    a=txt2.get()
    if (a==""):
        messagebox.showinfo(title="Alert", message="Enter Your Email Id")
    else:
        s1=student;
        s1.email=a
        import test_1

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

lbl = Label(root, text="EMAIL ID", width=20, height=2, fg="black",  font=('times', 15, ' bold '))
lbl.place(x=30, y=200)

lbl2 = Label(root, text="PASSWORD", width=20, fg="black",  height=2, font=('times', 15, ' bold '))
lbl2.place(x=30, y=275)

txt = Entry(root, validate="key", width=20, font=('times', 25, ' bold '))
txt.place(x=300, y=200)

txt2 = Entry(root, width=20, font=('times', 25, ' bold '))
txt2.place(x=300, y=275)

compare_dataset = Button(root, text="LOGIN",width=28  ,height=1,fg="#FFF",bg="#004080",command=training, activebackground = "orange",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=300, y=350)


message1 = Label(root, text="New User Register Here",
                     height=1, font=('Helvetica', 20, 'bold'))
message1.place(x=230, y=420)
message1.bind('<Button-1>', lambda *_: new_registration())

root.mainloop()

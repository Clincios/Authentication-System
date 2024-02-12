from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

def connection_database():
    if emailEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get()!=confirmEntry.get():
        messagebox.showerror('Error','Password Do Not Match')
    elif check.get()==0:
        messagebox.showerror('Error','Please Accept Terms $ Conditions')
    else:
        try:
            conn=pymysql.connect(host='localhost',user='root',password='Awine@23')
            mycursor=conn.cursor()
        except:
            messagebox.showerror('Error','Connection Failed, Please Try Again')
            return
        try:
            query = 'create database userdata1'
            mycursor.execute(query)
            query = 'use userdata1'
            mycursor.execute(query)
            query = 'create table data1(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata1')
        query='select * from data1 where username=%s'
        mycursor.execute(query,usernameEntry.get())

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error','Username Already Exist')
        else:
            query = 'insert into data1(email,username,password)values(%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('Success', 'Registration Is Successfull')
            clear()
            window.destroy()
            import LOgin
def next1():
    window.destroy()
    import LOgin

window=Tk()
window.title('SIGNUP')

bg=ImageTk.PhotoImage(file="C:/Users/AGEBOBA CLINTON/Desktop/bg.jpg")
bg_label=Label(window,image=bg)
bg_label.grid()

frame=Frame(window,bg='white')
frame.place(x=553,y=100)

header_label=Label(frame,text='CREATE AN ACCOUNT',bg='white',fg='firebrick1',font=('Microsoft Yahei UI Light','13','bold'))
header_label.grid(row=0,column=0,padx=35,pady=5)

emaillabel=Label(frame,text='Email',bg='white',fg='firebrick1',font=('Microsoft Yahei UI Light','13','bold'))
emaillabel.grid(row=1,column=0,sticky='w',padx=15,pady=(10,0))

emailEntry=Entry(frame,bg='firebrick1',fg='white',width=25,font=('Microsoft Yahei UI Light','13','bold'))
emailEntry.grid(row=2,column=0,sticky='w',padx=15)

usernamelabel=Label(frame,text='Username',bg='white',fg='firebrick1',font=('Microsoft Yahei UI Light','13','bold'))
usernamelabel.grid(row=3,column=0,sticky='w',padx=15,pady=(10,0))

usernameEntry=Entry(frame,bg='firebrick1',fg='white',width=25,font=('Microsoft Yahei UI Light','13','bold'))
usernameEntry.grid(row=4,column=0,sticky='w',padx=15)

passwordlabel=Label(frame,text='Password',bg='white',fg='firebrick1',font=('Micros0ft Yahei UI Light','13','bold'))
passwordlabel.grid(row=5,column=0,sticky='w',padx=15,pady=(10,0))

passwordEntry=Entry(frame,bg='firebrick1',fg='white',width=25,font=('Microsoft Yahei UI Light','13','bold'))
passwordEntry.grid(row=6,column=0,sticky='w',padx=15)

confirmlabel=Label(frame,text='Confirm Password',bg='white',fg='firebrick1',font=('Micros0ft Yahei UI Light','13','bold'))
confirmlabel.grid(row=7,column=0,sticky='w',padx=15,pady=(10,0))

confirmEntry=Entry(frame,bg='firebrick1',fg='white',width=25,font=('Microsoft Yahei UI Light','13','bold'))
confirmEntry.grid(row=8,column=0,sticky='w',padx=15)

check=IntVar()
check_button=Checkbutton(frame,text='I Agree To Terms And Conditions',activeforeground='firebrick1',activebackground='white',bg='white',fg='firebrick1',font=('Open Sans','9','bold'),variable=check)
check_button.grid(row=9,column=0,padx=10,pady=(10,0))

signup_button=Button(frame,text='Sign Up',cursor='hand2',bg='firebrick1',bd=0,fg='white',width=28,font=('open Sans','10','bold'),activebackground='firebrick1',activeforeground='white',command=connection_database)
signup_button.grid(row=10,column=0,pady=(20,0))

AlreadyAccount=Label(frame,text='Already Have An Account?',bg='white',fg='firebrick1',font=('Open Sans','9','bold'))
AlreadyAccount.grid(row=11,column=0,sticky='w',padx=20,pady=(60,0))

login_button=Button(frame,text='Login',cursor='hand2',bg='white',bd=0,fg='firebrick1',font=('open Sans','10','bold underline'),activebackground='white',activeforeground='firebrick1',command=next1)
login_button.grid(row=11,column=0,sticky='e',padx=20,pady=(60,0))

window.mainloop()

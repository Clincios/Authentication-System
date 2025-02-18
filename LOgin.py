from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def login_user():
    if username_entry.get()=='' or password_entry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    else:
        try:
            conn=pymysql.connect(host='localhost',user='root',password='Enter Your Password')
            mycursor=conn.cursor()
        except:
            messagebox.showerror('Error','Connection Failed, Please Try Again')
            return
        query='use userdata1'
        mycursor.execute(query)
        query='select * from data1 where username=%s and password=%s'
        mycursor.execute(query, (username_entry.get(),password_entry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid Username Or Password')
        else:
            messagebox.showinfo('Welcome','Login Is Suceessful')



def forget():
    window.destroy()
    import forget

def next1():
    window.destroy()
    import me
def on_enter(event):
    if username_entry.get()=='Username':
         username_entry.delete(0,END)

def enter(event):
    if password_entry.get() == 'Password':
        password_entry.delete(0, END)

def hash():
    openeye.config(file="C:/Users/AGEBOBA CLINTON/Desktop/closeye.png")
    password_entry.config(show='*')
    openeye_button.config(command=unhash)

def unhash():
    openeye.config(file="C:/Users/AGEBOBA CLINTON/Desktop/openeye.png")
    password_entry.config(show='')
    openeye_button.config(command=hash)



window=Tk()
# window.geometry("500x300")
login_image=ImageTk.PhotoImage(file="C:/Users/AGEBOBA CLINTON/Desktop/bg.jpg")
Labellogin_image=Label(window,image=login_image)
Labellogin_image.grid()


Header_label=Label(window,text="USER LOGIN",bg="white",fg='firebrick1',font=('Microsoft Yahei UI Light','16','bold'))
Header_label.place(x=630,y=100)

# username_label=Label(window,text='Username',bg='white',font=('Microsoft Yahei UI Light','12','bold'),fg='firebrick1')
# username_label.place(x=560,y=150)

username_entry=Entry(window,bd=0,width=28,font=('Microsoft Yahei UI Light','10','bold'),fg='firebrick1')
username_entry.place(x=560,y=180)
username_entry.insert(0,'Username')

Frame(window,width=250,height=3,bg='firebrick1').place(x=560,y=200)

password_entry=Entry(window,width=28,bd=0,font=('Microsoft Yahei UI Light','10','bold'),fg='firebrick1')
password_entry.place(x=560,y=250)
password_entry.insert(0,'Password')

Frame(window,width=250,bg='firebrick1',height=3).place(x=560,y=270)

login_button=Button(window,width=25,font=('Open Sans','11','bold'),text='Login',bg='firebrick1',fg='white',bd=0,activeforeground='white',activebackground='firebrick1',cursor='hand2',command=login_user)
login_button.place(x=573,y=330)

username_entry.bind('<FocusIn>',on_enter)
password_entry.bind('<FocusIn>',enter)

openeye=PhotoImage(file="C:/Users/AGEBOBA CLINTON/Desktop/closeye.png")
openeye_button=Button(window,image=openeye,cursor='hand2',bd=0,bg='white',activebackground='white',command=hash)
openeye_button.place(x=796,y=244)

forgot_button=Button(window,text='forgot password?',bg='white',bd=0,cursor='hand2',activebackground='white',activeforeground='firebrick1',font=('Microsoft Yahei UI Light','9','bold'),fg='firebrick1',command=forget)
forgot_button.place(x=695,y=290)

orlabel=Label(window,text='---------------Or--------------',bg='white',fg='firebrick1',font=('Open Sans','11','bold'))
orlabel.place(x=605,y=370)

google=PhotoImage(file="C:/Users/AGEBOBA CLINTON/Desktop/google.png")
google_label=Label(window,image=google,cursor='hand2',bg='white')
google_label.place(x=590,y=460)

facebook=PhotoImage(file="C:/Users/AGEBOBA CLINTON/Desktop/facebook.png")
facebook_label=Label(window,image=facebook,cursor='hand2',bg='white')
facebook_label.place(x=640,y=460)

twitter=PhotoImage(file="C:/Users/AGEBOBA CLINTON/Desktop/twitter.png")
twitter_label=Label(window,image=twitter,cursor='hand2',bg='white')
twitter_label.place(x=690,y=460)

signup_label=Label(window,text="Don't Have An Account?",bg='white',fg='firebrick1',font=('Open Sans','9','bold'))
signup_label.place(x=570,y=510)

signup_button=Button(window,text='Create Account',cursor='hand2',bg='white',bd=0,fg='firebrick1',font=('open Sans','9','bold underline'),activebackground='white',activeforeground='firebrick1',command=next1)
signup_button.place(x=740,y=510)

window.mainloop()

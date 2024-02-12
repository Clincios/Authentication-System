from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import ImageTk

def forget():
    if usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get()!=confirmEntry.get():
        messagebox.showerror('Error','Password Do Not Match')
    else:
        conn = pymysql.connect(host='localhost', user='root', password='Awine@23',database='userdata1')
        mycursor = conn.cursor()
        query='select * from data1 where username=%s'
        mycursor.execute(query,(usernameEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Incorrect Username')
        else:
            query='update data1 set password=%s where username=%s'
            mycursor.execute(query,(passwordEntry.get(),usernameEntry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('Success','Password Is Reset Successfully, Please Login With New Password')

    window.destroy()
    import LOgin

window = Tk()
window.title('forget')

bg=ImageTk.PhotoImage(file='C:/Users/AGEBOBA CLINTON/Desktop/background.jpg')
bg_label=Label(window,image=bg)
bg_label.grid()

headerlabel=Label(window,text='RESET PASSWORD',font=('Open Sans','14','bold'),bg='white',fg='purple')
headerlabel.place(x=515,y=50)

usernamelabel=Label(window,text='Username',font=('Microsoft Yahei UI Light','10','bold'),bg='white',fg='purple')
usernamelabel.place(x=475,y=120)
usernameEntry=Entry(window,width=31,fg='purple',bd=0,font=('Microsoft Yahei UI Light','10','bold'))
usernameEntry.place(x=475,y=160)
frame=Frame(window,width=250,height=2,bg='purple').place(x=475,y=185)

passwordlabel=Label(window,text='Password',font=('Microsoft Yahei UI Light','10','bold'),bg='white',fg='purple')
passwordlabel.place(x=475,y=220)
passwordEntry=Entry(window,width=31,fg='purple',bd=0,font=('Microsoft Yahei UI Light','10','bold'))
passwordEntry.place(x=475,y=255)
frame=Frame(window,width=250,height=2,bg='purple').place(x=475,y=275)

confirmlabel=Label(window,text='Confirm Password',font=('Microsoft Yahei UI Light','10','bold'),bg='white',fg='purple')
confirmlabel.place(x=475,y=310)
confirmEntry=Entry(window,width=31,fg='purple',bd=0,font=('Microsoft Yahei UI Light','10','bold'))
confirmEntry.place(x=475,y=345)
frame=Frame(window,width=250,height=2,bg='purple').place(x=475,y=365)

forgetbutton=Button(window,text='Submit',width=27,bg='purple',bd=0,fg='white',font=('Microsoft Yahei UI Light','10','bold'),activeforeground='white',activebackground='purple',command=forget,cursor='hand2')
forgetbutton.place(x=475,y=420)

window.mainloop()

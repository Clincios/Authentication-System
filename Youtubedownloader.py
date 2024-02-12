from tkinter import *
from tkinter import messagebox
from pytube import YouTube

def youdownload():
    link=entry_box.get()
    try:
        yn=YouTube(link)
        yn = yn.streams.get_highest_resolution()
        yn.download()
        messagebox.showinfo('Success','Download Completed')
    except:
        messagebox.showerror('Error','Invalid Url')

window=Tk()
window.geometry("600x400")
window.title("YOUTUBE DOWNLOADER")
window.resizable('false','false')
window.configure(bg="white")

frame1=Frame(window,bg="cyan",relief=GROOVE,bd=5)
frame1.pack(pady=80)

label1=Label(frame1,text="YouTube Video Downloader",font=('Microsoft Yahei UI Light','25','bold'),bg="cyan",fg="firebrick2")
label1.pack(padx=10,pady=5)

label2=Label(frame1,text="Enter URL Link Of Video To Download",font=('Microsoft Yahei UI Light','12','bold'),bg="cyan",fg="firebrick2")
label2.pack(pady=20)

entry_box=Entry(frame1,width=60,font=('Microsoft Yahei UI Light','10','bold'),bg="white",fg="firebrick2",justify='center')
entry_box.pack(pady=5)

button1=Button(frame1,text="Download",width=20,bg="cyan",fg="firebrick2",activebackground="cyan",activeforeground="cyan",bd=2,font=('Microsoft Yahei UI Light','10','bold'),command=youdownload)
button1.pack(pady=5)


window.mainloop()
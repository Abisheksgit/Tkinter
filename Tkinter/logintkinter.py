from tkinter import *
import tkinter
from tkinter.font import Font
from tkinter import messagebox

window=Tk()
window.title("Login Form")
window.geometry('500x500')
window.configure(bg='black')
#window.attributes('-transparentcolor','black')

def login():
    username="abishek" 
    password="12345"
    username="ram"
    password="123"
    username="ram"
    password="000"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success",message="You Successfilly Logged in")
    else:
        messagebox.showerror(title="Error",message="Invalid Login")

#tkinter container
frame=tkinter.Frame(bg='black')

myfont=Font(family="Arial",size=30)
myfont2=Font(family="Arial",size=16)
myfont3=Font(family="Arial",size=10)

#creating widets
login_label=Label(frame, text="Login",bg='black',fg='#FF3399',font=myfont)
username_label=Label(frame, text="Username",bg='black',fg='#FFFFFF',font=myfont2)
username_entry=Entry(frame,font=myfont2)
password_entry=Entry(frame, show="*",font=myfont2)
password_label=Label(frame, text="Password",bg='black',fg='#FFFFFF',font=myfont2)
login_button=Button(frame, text="Login",bg='#FF3399',fg='#FFFFFF',font=myfont2,command=login)


#Placing widgets on the screen 
login_label.grid(row=0, column=0, columnspan=2,pady=100)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1,pady=30)
login_button.grid(row=3, column=0, columnspan=2,pady=80)

#window.config(bg='black')
frame.pack()

window.mainloop()
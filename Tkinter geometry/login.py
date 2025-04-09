from tkinter import *

root=Tk()
root.title("login page")
root.geometry("400x400")

frame=Frame(master=root,height=200,width=360,bg="#d0efff")

lbl1=Label(frame,text="Full name",bg="#3895D3",fg="white",width=12)
lbl2=Label(frame,text="E-mail",bg="#3895D3",fg="white",width=12)
lbl3=Label(frame,text="Password",bg="#3895D3",fg="white",width=12)

name_entry=Entry(frame)
email_entry=Entry(frame)
pass_entry=Entry(frame,show="*")

def display():
    name=name_entry.get()
    greet="Hey "+ name
    message="\n congratulations your account is created"
    textbox.insert(END,greet)
    textbox.insert

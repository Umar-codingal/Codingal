from tkinter import *
from datetime import date

root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=300)

name_lbl = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()

    global message
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello " + name + "\n"

    
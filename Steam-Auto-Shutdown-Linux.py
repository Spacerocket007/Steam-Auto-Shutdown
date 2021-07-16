#!/usr/bin/python
import os
from os import listdir
from tkinter import *
from tkinter import filedialog
import sys
from tkinter import(
    Tk, Button, Label, StringVar, Entry, END,
)


root = Tk()
root.title("Auto Shutdown Steam")
root.geometry('550x300')
root.configure(bg='cornflower blue')
root.configure(bg='cornflower blue')
root.resizable(False, False)


def cancel():
    os.system("shutdown -c")
    L1.config(text="shutdown canceled!")
    button2.destroy
    button3.place(x="180", y="80")
    root.after(2000, destroy)


def destroy():
    root.destroy()


def search():
    file_path=filedialog.askdirectory()
    os.listdir(file_path)
    if len(os.listdir(file_path)) == 0:
        L3.place(x="-80", y="80")
        L4.place(x="-80", y="120")
        button1.destroy()
        print("Error")
    for file_name in listdir(file_path):    
        if not file_name.endswith(".abcde"):
            button1.destroy()
            L2.place(x="140", y="120")
            def loop():
                 os.listdir(file_path)
                 if len(os.listdir(file_path)) == 0:
                     print("shutdown")
                     os.system("shutdown -h 1")
                     L2.destroy()
                     button1.destroy()
                     L1.pack(side="bottom")
                     button2.place(x="180", y="80")
                 root.after(5000, loop)
            loop()
button2 = Button(root, text="cancel shutdown", bg="white", fg="black", command=cancel, height=5, width=20, font="bold")
button3 = Button(root, text="canceled", bg="white", fg="black", command=cancel, height=5, width=20, font="bold")
L1 = Label(root, text="OS will shutdown in 1min!", bg='cornflower blue', fg="red", font="bold", height=2, width=30)
button1 = Button(root, text="Please select your steam download folder", bg="white", fg="black", command=search,height=10, width=50, font="bold")
L2 = Label(root, text="Waiting for download to finish...", bg="cornflower blue", fg="black", height=2, width=30, font="bold")
L3 = Label(root, text="ERROR: 404 ", bg="cornflower blue",fg="black", height=2, width=80, font="bold")
L4 = Label(root, text="Folder is empty! D: Is Steam downloading!? Please restart this App", bg="cornflower blue",fg="black", height=2, width=80, font="bold")
button1.pack(pady=30)


root.mainloop()

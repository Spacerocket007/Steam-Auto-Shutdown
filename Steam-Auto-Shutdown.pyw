import os
from os import listdir
from tkinter import *
from tkinter import filedialog
import sys
from tkinter import(
    Tk, Button, Label, StringVar, Entry, END,
)
from tkinter.ttk import Progressbar

root = Tk()
root.title("Steam Auto Shutdown")
root.geometry('550x300')
root.configure(bg='#2a475e')
root.resizable(False, False)


def cancel():
    os.system("shutdown -a")
    L1.config(text="shutdown canceled!")
    button2.destroy
    button3.place(x="170", y="100")
    root.after(2000, destroy)


def destroy():
    root.destroy()


def search():
    file_path=filedialog.askdirectory()
    os.listdir(file_path)
    if len(os.listdir(file_path)) == 0:
        L3.place(x="-130", y="80")
        L4.place(x="-130", y="120")
        button1.destroy()
        print("Error")
    for file_name in listdir(file_path):    
        if not file_name.endswith(".abcde"):
            button1.destroy()
            L2.place(x="120", y="120")
            L5.pack(side="bottom")
            def loop():
                 os.listdir(file_path)
                 if len(os.listdir(file_path)) == 0:
                     print("shutdown")
                     os.system("shutdown /s /t 60")
                     L2.destroy()
                     L5.destroy()
                     button1.destroy()
                     L1.pack(side="bottom")
                     button2.place(x="170", y="100")
                 root.after(5000, loop)
            loop()

button1 = Button(root, text="Please select your steam download folder", bg="#515252", fg="white", command=search,height=1, width=35, font="sans 13 bold")
button2 = Button(root, text="cancel shutdown", bg="#515252", fg="white", command=cancel, height=3, width=20, font="sans 12 bold")
button3 = Button(root, text="canceled", bg="#515252", fg="white", command=cancel, height=3, width=20, font="sans 12 bold")
L1 = Label(root, text="OS will shutdown in 1min!", bg='#2a475e', fg="red", font="sans 12 bold", height=2, width=30)
L2 = Label(root, text="Waiting for downloads to finish...", bg="#2a475e", fg="black", height=2, width=30, font="sans 13 bold")
L3 = Label(root, text="ERROR: 404 ", bg="#2a475e",fg="black", height=2, width=80, font="sans 12 bold")
L4 = Label(root, text="Folder is empty! D: Is Steam downloading!? Please restart this App", bg="#2a475e",fg="black", height=2, width=80, font="sans 12 bold")
L5 = Label(root, text="Computer will shutdown after all downloads finish", bg='#2a475e', fg="black", font="bold", height=1, width=40)
L6 = Label(root, text="Created by github.com/Spacerocket007", bg='#2a475e', fg="white", font="sans 9 bold", height=0, width=40)
button1.pack(pady=110)
L6.place(x="-30", y="0")

root.mainloop()

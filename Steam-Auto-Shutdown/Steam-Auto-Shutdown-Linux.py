#!/usr/bin/python
import os
from os import listdir
from tkinter import *
from tkinter import filedialog
from tkinter import (
    Tk, Button, Label,
)



root = Tk()
root.title("Steam Auto Shutdown")
root.geometry('550x300')
root.configure(bg='#2a475e')
root.resizable(False, False)
status = True
check = False
bg = PhotoImage(file="background.png")
background = Label(root, image=bg)
background.place(relheight=1, relwidth=1, x="0", y="0")

def cancel():
    os.system("shutdown -c")
    L1.config(text="shutdown canceled!")
    button2["text"] = "canceled"
    root.after(2000, destroy)


def destroy():
    root.destroy()


def search():
    global file_path
    file_path = filedialog.askdirectory()
    if len(os.listdir(file_path)) == 0:
        L7.destroy()
        L10.destroy()
        L11.destroy()        
        button1.destroy()
        L3.place(x="-130", y="80")
        L4.place(x="-130", y="120")
        L8.place(x="495", y="0")
    for file_name in listdir(file_path):
        if not file_name.endswith(".abcde"):
            Status_label.place(x="350", y="113")
            Toggle_Button.place(x="180", y="100")
            button4.place(x="180", y="170")
            switch()


def switch():
    global status
    global check
    button1.destroy()
    L8.place(x="495", y="0")
    L7.destroy()
    L10.destroy()
    L11.destroy()    
    if status:
        Status_label.config(text="Off", fg="red")
        status = False
        check = False
        loop()

    else:
        Status_label.config(text="On", fg="green")
        status = True
        check = True
        L9.place(x="-10", y="280")
        loop()


def loop():
    if check == True:
        os.listdir(file_path)
        if len(os.listdir(file_path)) == 0:
            os.system("shutdown -h 1")
            L5.destroy()
            L9.destroy()
            button4.destroy()
            Toggle_Button.destroy()
            Status_label.destroy()
            button1.destroy()
            L1.pack(side="bottom")
            button2.place(x="170", y="100")
        L9.configure(text="refreshed")
        root.after(1000, clear)
    else:
        root.after(5000, loop)


def clear():
    L9["text"] = ""
    root.after(4000, loop)


button1 = Button(root, text="Please select in your steam folder 'downloading'", bg="#515252", fg="white", command=search,
                 height=1, width=40, font="sans 13 bold", bd=1)
button2 = Button(root, text="cancel shutdown", bg="#515252", fg="white", command=cancel, height=3, width=20, bd=1,
                 font="sans 12 bold")
button3 = Button(root, text="canceled", bg="#515252", fg="white", command=cancel, height=3, width=20,
                 font="sans 12 bold", bd=1)
button4 = Button(root, text="Exit", bg="#515252", fg="white", command=destroy, height=2, width=20, font="sans 12 bold", bd=1)
Toggle_Button = Button(root, text="Toggle On/Off", bg="#515252", fg="white", height=2, width=20, font="sans 12 bold",
                       bd=1, command=switch)
L1 = Label(root, text="OS will shutdown in 1min!", bg='grey', fg="red", font="sans 12 bold", height=0, width=20)
L3 = Label(root, text="ERROR: 404 ", bg="red", fg="black", height=2, width=80, font="sans 12 bold")
L4 = Label(root, text="Folder is empty! D: Is Steam downloading!? Please restart this App", bg="red", fg="black",
           height=2, width=80, font="sans 12 bold")
L5 = Label(root, text="Computer will shutdown after all downloads finish", bg='#2a475e', fg="black", font="bold",
           height=1, width=40)
L6 = Label(root, text="Created by https://github.com/Spacerocket007/", bg='grey', fg="white", font="sans 9 bold", height=0,
           width=40)
L7 = Label(root, text="Steam Auto Shutdown v2.1", bg='grey', fg="white", font="sans 12 bold", height=0, width=20)
L8 = Label(root, text="v2.1", bg='grey', fg="white", font="sans 9 bold", height=0, width=5)
L9 = Label(root, text="refreshed", bg='grey', fg="green", font="sans 9 bold", height=0, width=10)
L10 = Label(root, text="This is required to show the program where games are downloaded", bg="grey", fg="white", font="sans 8 bold", height=0, width=55)
Status_label = Label(root, text="On!", fg="green", bg='#515252', font="sans 12 bold")
L11 = Label(root, text="and once they are grabbed, to turn off your Computer", bg="grey", fg="white", font="sans 8 bold", height=0, width=45)
Status_label = Label(root, text="On!", fg="green", bg='#515252', font="sans 12 bold")
button1.pack(pady=110)
Status_label = Label(root, text="On!", fg="green", bg='#515252', font="sans 12 bold")
button1.pack(pady=110)
L7.pack(pady=0)
L6.place(x="-10", y="0")
L10.place(x="80", y="150")
L11.place(x="110", y="170")
root.mainloop()

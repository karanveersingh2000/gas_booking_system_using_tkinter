# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:33:28 2020

@author: Karanveer singh
"""
from tkinter import *

from tkinter import messagebox
from lpgsys import *


import mysql.connector
from PIL import ImageTk,Image



def check():
    cn = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='gas_booking')
    cur=cn.cursor()
    st="select * from customer where customer_name='{}' and password='{}'".format(t1.get(),t2.get())
    cur.execute(st)
    x=cur.fetchall()
    if len(x)==1:
        messagebox.showinfo("Say Hello", "login successful")
        sys()
    else:
        messagebox.showinfo("Say Hello", "invalid username or password")

    cn.close()


def login(sc):
    global t1
    global t2
    t1=StringVar()
    t2=StringVar()
    sc1= Toplevel(sc)
    sc1.geometry("1000x1000")
    sc1.configure(bg="light grey")
         
    load = Image.open("gas1.jpg")
    rr = ImageTk.PhotoImage(load)

    img = Label(sc1, image=rr,bg="light grey")
    img.image = rr
    img.place(x=0, y=260)
    Label(sc1,text="GAS BOOKING ",bg="light grey",font=("arial",40)).grid(row=0,column= 0)
    Label(sc1,text="USERNAME",bg="light grey",font=("arial", 20)).grid(row =8,column=0)
    tt1=    Entry(sc1,textvariable=t1)
    tt1.grid(row=8,column=1)
    Label(sc1,text ="PASSWORD",bg="light grey",font=("arial", 20)).grid(row =10,column=0)
    tt2=    Entry(sc1,textvariable=t2)
    tt2.grid(row=10,column=1)
    b1=Button(sc1,text ="SIGN IN",font=("arial",15),fg="white",height = 3, width= 15,bg="black",command=check)
    b1.grid(row=12,column=0)
    sc1.mainloop()

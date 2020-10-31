# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 08:24:22 2020

@author: Karanveer singh
"""

from tkinter import*
from datetime import date
from datetime import timedelta
from tkinter import messagebox
import mysql.connector
def detail():
   
    cn = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='gas_booking')
   
    cur=cn.cursor()          
    amt=700
    today = date.today()
    new_date = today + timedelta(6)
    
    print(today, new_date, tt1.get())
   
    st="insert into booking_details(amount,booking_date,delivery_date,cust_id) values ({},'{}','{}','{}')".format(amt,today,new_date,tt1.get())
    cur.execute(st)
    cn.commit() 




def sys():
    global t1
    global tt1
    t1=IntVar()
    root=Tk()
    root.geometry("1000x1000")
    l1=Label(root,text="HELLO" ,font=("Arial",50))
    
    l2=Label(root,text="ENTER CUSTOMER_ID ",font=("arial",40))
    l2.place(x=0,y=100)
    tt1=Entry(root,textvariable=t1)
    tt1.place(x=600,y=125)
   

    
    B1=Button(root,text="Book Your Gas",font=("arial",25),command =lambda:[detail(),confirm()])
    B1.place(x=400,y=200)
   
    l1.place(x=400,y=0)
    root.mainloop()
def mess():
    messagebox.showinfo("CONFIRMATION","BOOKING CONFIRMED")


    
def confirm():
    top = Tk()
    c1 = IntVar()
    C1 = Radiobutton(top, text="BOOK YOUR GAS FOR 700.00 RUPEES", variable=c1,font=("arial",25))
    B1=Button(top,text="SELECT & CONFIRM",font=("arial",25),command=mess)
    B1.pack()
    C1.pack()
    top.mainloop()

        
    
    
   
  

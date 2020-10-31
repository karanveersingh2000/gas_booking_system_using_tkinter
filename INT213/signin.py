# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 16:03:00 2020

@author: Karanveer singh
"""
from tkinter import*
import mysql.connector
from PIL import ImageTk,Image
from login import*
from lpgsys import*

def ADD():
    cn = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='gas_booking')
    cur=cn.cursor()
    st="insert into customer (CUSTOMER_NAME,ADDRESS,CITY,ZIP_CODE,PHONE_NO,ADHAR_NO,PASSWORD) values  ('{}','{}','{}','{}','{}','{}','{}')".format(t1.get(),t2.get(),t3.get(),t4.get(),t6.get(),t5.get(),t7.get())
    cur.execute(st)
    cn.commit()
    
    
     

    
  
    cn.close()
def signin(sc):
    global t1
    global t2
    global t3
    global t4
    global t5
    global t6
    global t7
    t1=StringVar()
    
    t2=StringVar()
    t3=StringVar()
    t4=StringVar()
    t5=StringVar()
    t6=StringVar()
    t7=StringVar()
    
        
    
    sc1= Toplevel(sc)
    sc1.geometry("1000x1000")
    sc1.configure(bg="light grey")
       
  

    
    Label(sc1,text="GAS BOOKING ",bg="light grey",font=("arial",50)).place(x=250,y=0)
    Label(sc1,text="FULL NAME",bg="light grey",font=("arial", 20)).place(x=250,y=100)
    tt1=    Entry(sc1,textvariable=t1)
    tt1.place(x=600,y=110)
    Label(sc1,text ="ADDRESS",bg="light grey",font=("arial", 20)).place(x=250,y=150)
    tt2=    Entry(sc1,textvariable=t2)
    tt2.place(x=600,y=160)
    
    Label(sc1,text ="CITY",bg="light grey",font=("arial", 20)).place(x=250,y=200)
    tt3=    Entry(sc1,textvariable=t3)
    tt3.place(x=600,y=210)
    Label(sc1,text ="ZIP CODE",bg="light grey",font=("arial", 20)).place(x=250,y=250)
    tt4=    Entry(sc1,textvariable=t4)
    tt4.place(x=600,y=260)
    Label(sc1,text ="ADHAR CARD NUMBER",bg="light grey",font=("arial", 20)).place(x=250,y=300)
    tt5=    Entry(sc1,textvariable=t5)
    tt5.place(x=600,y=310)
    Label(sc1,text="PHONE NO.",bg="light grey",font=("arial", 20)).place(x=250,y=350)
    tt6=    Entry(sc1,textvariable=t6)
    tt6.place(x=600,y=360)
    Label(sc1,text ="PASSWORD",bg="light grey",font=("arial", 20)).place(x=250,y=400)
    tt7=    Entry(sc1,textvariable=t7)
    tt7.place(x=600,y=410)
    b1=Button(sc1,text ="REGISTER",font=("arial",15),fg="white",height = 3, width= 15,bg="black",command=ADD)
    b1.place(x=250,y=500)
    Label(sc1,text="Press LOGIN PAGE After Clicking REGISTER").place(x=250,y=580)
    b1=Button(sc1,text ="LOGIN PAGE ",font=("arial",15),fg="white",height = 3, width= 15,bg="black",command = lambda:login(sc))
    b1.place(x=250,y=650)
    sc1.mainloop()
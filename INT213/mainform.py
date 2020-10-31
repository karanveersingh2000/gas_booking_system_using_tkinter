# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:38:20 2020

@author: Karanveer singh
"""

from tkinter import*
from login import*
from signin import*
from PIL import ImageTk,Image 

sc = Tk()
sc.geometry("750x760")
sc.configure(bg="light grey")
canvas = Canvas(sc, width = 750, height = 760)      
canvas.place(x=0,y=0)      
img = PhotoImage(file="lpg.png")      
canvas.create_image(20,20, anchor=NW, image=img)  


Label(sc,text="WELCOME TO GAS BOOKING  ",font=("arial",40),bg="light grey").grid(row=0,column=3)
B1 = Button(sc, text = "register ",font=("arial",15), height=3,width=20,command = lambda:signin(sc))
B1.place(x=0,y=660)
B2 = Button(sc, text = "login ",font=("arial",15), height=3,width=20,command = lambda:login(sc))
B2.place(x=520,y=660)
sc.mainloop()
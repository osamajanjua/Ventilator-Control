import struct
import time
import sys
import random
import serial
from tkinter import *
from tkinter import ttk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

window = Tk()
window.title("Ventilator")
window.geometry("1024x768+0+0")
window.configure(background="black")

#arduino_data=serial.Serial('COM5',baudrate=9600)
#time.sleep(2)

BPM_entry_counter=0
def enter_BPM():
    global display_BPM
    global BPM_entry_counter
    BPM_value=int(BPM.get())
    upper_limit_BPM_value=int(upper_limit_BPM.get())
    lower_limit_BPM_value=int(lower_limit_BPM.get())
    x_coor=200;y_coor=50
    if BPM_entry_counter>0:
        display_BPM.place_forget()
    if lower_limit_BPM_value<=BPM_value<=upper_limit_BPM_value:
        displayed_string_BPM= str(BPM_value) + " Breaths Per Minute"
        display_BPM=Label(window, text=(displayed_string_BPM),bg="#262626", fg="white", font=("montserrat",14,"normal"))
        display_BPM.place(x=x_coor,y=y_coor)
        BPM_entry_counter=BPM_entry_counter+1
        #send_BPM_to_arduino()
    if BPM_value>upper_limit_BPM_value:
        display_BPM=Label(window, text=("o bhai banda ventilator par hai cycle par nai"),bg="#262626", fg="white", font=("montserrat",14,"normal"))
        display_BPM.place(x=x_coor,y=y_coor)
        BPM_entry_counter=BPM_entry_counter+1
    if BPM_value<lower_limit_BPM_value:
        display_BPM=Label(window, text=("haan agla toh pro swimmer hai na"),bg="#262626", fg="white", font=("montserrat",14,"normal"))
        BPM_entry_counter=BPM_entry_counter+1
        display_BPM.place(x=x_coor,y=y_coor)
BPM=StringVar()
lower_limit_BPM=StringVar(); upper_limit_BPM=StringVar()
lower_limit_BPM_entry=Entry(window,textvariable=lower_limit_BPM,width=5,bg="white")
upper_limit_BPM_entry=Entry(window,textvariable=upper_limit_BPM,width=5,bg="white")
lower_limit_BPM_entry.place(x=400,y=200)
upper_limit_BPM_entry.place(x=400+75,y=200)

Update_BPM=Button(window,text="Update BPM", font=("montserrat",10,"bold"), width=14, bg="white",fg="black",command=enter_BPM)
BPM_value_entry=Entry(window,textvariable=BPM,width=4,bg="white")
BPM_value_entry.place(x=150,y=205)

Update_BPM.place(x=200,y=202)
BPM_text=Label(window, text="BPM: ", bg="#262626", fg="white",font=("montserrat",14,"normal"))
BPM_text.place(x=30,y=200)




window.mainloop()

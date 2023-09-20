import struct
import time
import sys
import random
import serial
from tkinter import *
from tkinter import ttk


window = Tk()
window.title("Ventilator")
window.geometry("1024x768+0+0")
window.configure(background="#262626")
arduino_data=serial.Serial('COM3',baudrate=9600)
time.sleep(2)
counter=0
def data_printer():
    global counter
    counter=counter+1
    input=arduino_data.readline()
    opened_string=str(input).split('P')
    print(str(opened_string[0]))
    # print(input)
    # lab=Label(window, text=input, bg="#262626", fg="white",font=("montserrat",34,"normal"))
    # lab.place(x=5,y=50)
    if counter<50:
        window.after(1, data_printer)
#window.after(1, data_printer)
data_printer()
window.mainloop()

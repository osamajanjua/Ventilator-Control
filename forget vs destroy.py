from tkinter import *
from tkinter import ttk
import time
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


scaling="not"
property_being_updated="none"
unit_of_property_being_updated="none"
value_pressure_entered=0
value_vol_entered=0
value_peep_entered=0
value_bpm_entered=0
value_oxygen_entered=0

window = Tk()
window.title("Ventilator")
window.geometry("1024x768+0+0")
window.configure(background="black")

style = ttk.Style(window)

def makeandbreak():
    global logo
    logo_image=PhotoImage(file="logo.gif")
    logo=Label(window, text=1, bg="black", fg="white",font=("montserrat light",12,"normal"))
    logo.place(x=700,y=10)
    print("p")
    conf()
global i
i=0
def conf():
    global i
    global logo
    logo.configure(text=1+i)
    i=i+1
    window.after(1000,conf)
makeandbreak()

window.mainloop()

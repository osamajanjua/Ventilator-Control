from tkinter import *
from tkinter import ttk
#from making_monitoring_function import display_Peak_Pressure
import making_monitoring_function as m1
#import vent1.py

window = Tk()
window.title("Ventilator")
window.geometry("1024x768+0+0")
window.configure(background="black")


print("a")
m1.display_Peak_Pressure(35,40,5)

window.mainloop()

from tkinter import *
from tkinter import ttk
import custom_scale_main_and_outta_loop as cs

window = Tk()
window.title("Ventilator")
window.geometry("1024x768+0+0")
window.configure(background="black")
update_pressure_button_image=PhotoImage(file="update_p.gif")
update_pressure_image_properties=Label(window, image=update_pressure_button_image, bg="black")
update_pressure_button=Button(window, image=update_pressure_button_image, highlightthickness=0,bd=0,bg="white",command=cs.update_pressure())
update_pressure_button.place(x=1,y=1)
cs.tf()

window.mainloop()

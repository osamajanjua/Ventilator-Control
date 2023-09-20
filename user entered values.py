from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Ventilator")
window.geometry("1024x768+0+0")
window.configure(background="black")


def enter_tidal_vol():
    print('x')
x_increment=0
tidal_vol=StringVar()
lower_limit_tidal_vol=StringVar(); upper_limit_tidal_vol=StringVar()
tidal_vol_value_entry=Entry(window,textvariable=tidal_vol,width=15,bg="white")
lower_limit_tidal_vol_entry=Entry(window,textvariable=lower_limit_tidal_vol,width=5,bg="white")
upper_limit_tidal_vol_entry=Entry(window,textvariable=upper_limit_tidal_vol,width=5,bg="white")
update_vol_button_image=PhotoImage(file="update_vol.gif")
update_vol_image_properties=Label(window, image=update_vol_button_image, bg="black")
update_vol_button=Button(window, image=update_vol_button_image, highlightthickness=0,bd=0,bg="white",command=enter_tidal_vol)
tidal_vol_value_entry.place(x=80,y=240)
lower_limit_tidal_vol_entry.place(x=80,y=262)
upper_limit_tidal_vol_entry.place(x=140,y=262)
update_vol_button.place(x=190+x_increment,y=239)

#Update_tidal_vol.place(x=200,y=202+35+35+35)
tidal_text=Label(window, text="Vol", bg="black", fg="white",font=("montserrat light",13,"normal"))
unit_text=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",9,"normal"))
tidal_text.place(x=30,y=235)
unit_text.place(x=30,y=260)



window.mainloop()

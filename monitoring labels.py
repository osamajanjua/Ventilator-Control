from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Ventilator")
window.geometry("1024x768+0+0")
window.configure(background="black")


def display_Peak_Pressure(Peak_Pressure,max,min):
    line_number=1
    line=line_number-1
    x_increment=0; y_increment=65
    number=Label(window, text=Peak_Pressure, bg="black", fg="white",font=("montserrat",34,"normal"))
    what_it_is=Label(window, text="Peak Pressure", bg="black", fg="white",font=("montserrat light",12,"normal"))
    unit=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",12,"normal"))
    maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
    minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
    number.place(x=120+x_increment,y=40+line*y_increment)
    what_it_is.place(x=185,y=47+line*y_increment)
    unit.place(x=185+x_increment,y=68+line*y_increment)
    maximum.place(x=45+x_increment,y=50+line*y_increment)
    minimum.place(x=45+x_increment,y=70+line*y_increment)

def display_BPM(BPM,max,min):
    line_number=2
    line=line_number-1
    x_increment=0; y_increment=65
    number=Label(window, text=BPM, bg="black", fg="white",font=("montserrat",34,"normal"))
    what_it_is=Label(window, text="BPM", bg="black", fg="white",font=("montserrat light",12,"normal"))
    maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
    minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
    number.place(x=120+x_increment,y=40+line*y_increment)
    what_it_is.place(x=185+x_increment,y=47+line*y_increment)
    maximum.place(x=45+x_increment,y=50+line*y_increment)
    minimum.place(x=45+x_increment,y=70+line*y_increment)

def display_Flow(Flow,max,min):
    line_number=3
    line=line_number-1
    x_increment=0; y_increment=65
    number=Label(window, text=Flow, bg="black", fg="white",font=("montserrat",34,"normal"))
    what_it_is=Label(window, text="Flow", bg="black", fg="white",font=("montserrat light",12,"normal"))
    unit=Label(window, text="L/min", bg="black", fg="white",font=("montserrat light",12,"normal"))
    maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
    minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
    number.place(x=120+x_increment,y=40+line*y_increment)
    what_it_is.place(x=185+x_increment,y=47+y_increment)
    unit.place(x=185+x_increment,y=68+line*y_increment)
    maximum.place(x=45+x_increment,y=50+line*y_increment)
    minimum.place(x=45+x_increment,y=70+line*y_increment)

def display_VTE(VTE,max,min):
    line_number=4
    line=line_number-1
    x_increment=0; y_increment=65
    number=Label(window, text=VTE, bg="black", fg="white",font=("montserrat",34,"normal"))
    what_it_is=Label(window, text="VTE", bg="black", fg="white",font=("montserrat light",12,"normal"))
    unit=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",12,"normal"))
    maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
    minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
    number.place(x=90+x_increment,y=40+line*y_increment)
    what_it_is.place(x=185+x_increment,y=47+line*y_increment)
    unit.place(x=185+x_increment,y=68+line*y_increment)
    maximum.place(x=45+x_increment,y=50+line*y_increment)
    minimum.place(x=45+x_increment,y=70+line*y_increment)

def display_IE(IE,max,min):
    line_number=5
    line=line_number-1
    x_increment=0; y_increment=65
    number=Label(window, text="1:"+str(IE), bg="black", fg="white",font=("montserrat",34,"normal"))
    what_it_is=Label(window, text="IE Ratio", bg="black", fg="white",font=("montserrat light",12,"normal"))
    maximum=Label(window, text="1:"+str(max), bg="black", fg="white",font=("montserrat light",10,"normal"))
    minimum=Label(window, text="1:"+str(min), bg="black", fg="white",font=("montserrat light",10,"normal"))
    number.place(x=120+x_increment,y=40+line*y_increment)
    what_it_is.place(x=185+x_increment,y=47+line*y_increment)
    maximum.place(x=45+x_increment,y=50+line*y_increment)
    minimum.place(x=45+x_increment,y=70+line*y_increment)


display_Peak_Pressure(35,32,2)
display_BPM(21,32,2)
display_Flow(8.1,32,2)
display_VTE(900,1400,500)
display_IE(2,1.5,1.25)







def update_tidal_vol():
    print('x')
line_number=1
line=line_number-1
x_increment=1200; y_increment=0
tidal_vol=StringVar()
lower_limit_tidal_vol=StringVar(); upper_limit_tidal_vol=StringVar()
tidal_vol_value_entry=Entry(window,textvariable=tidal_vol,width=15,bg="white")
lower_limit_tidal_vol_entry=Entry(window,textvariable=lower_limit_tidal_vol,width=5,bg="white")
upper_limit_tidal_vol_entry=Entry(window,textvariable=upper_limit_tidal_vol,width=5,bg="white")
update_vol_button_image=PhotoImage(file="update_vol.gif")
update_vol_image_properties=Label(window, image=update_vol_button_image, bg="black")
update_vol_button=Button(window, image=update_vol_button_image, highlightthickness=0,bd=0,bg="white",command=update_tidal_vol)
tidal_text=Label(window, text="Vol", bg="black", fg="white",font=("montserrat light",13,"normal"))
unit_text=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",9,"normal"))
tidal_vol_value_entry.place(x=80+x_increment,y=40+y_increment)
lower_limit_tidal_vol_entry.place(x=80+x_increment,y=62+y_increment)
upper_limit_tidal_vol_entry.place(x=140+x_increment,y=62+y_increment)
update_vol_button.place(x=190+x_increment,y=39+y_increment)
tidal_text.place(x=30+x_increment,y=35+y_increment)
unit_text.place(x=30+x_increment,y=60+y_increment)









window.mainloop()

from tkinter import *
import tkinter as tk
from tkinter import ttk
y_inc=600

scale_location_x=300
scale_location_y=10+y_inc
scale_value_location_x=740-10-8+30
scale_value_location_y=120+30+y_inc-21
scale_label_location_x=720+30
scale_label_location_y=120+y_inc-21
scale_value_unit_location_x=730-10+30
scale_value_unit_location_y=170+13+y_inc-21
cross_location_x=200
cross_location_y=30+y_inc
tick_location_x=cross_location_x+1100
tick_location_y=cross_location_y
scaling="not"
property_being_updated="none"
unit_of_property_being_updated="none"
value_pressure=0
value_vol=0
value_peep=0
value_bpm=0
update_pressure_button_x=100
update_pressure_button_y=200
update_vol_button_x=100
update_vol_button_y=300
update_bpm_button_x=100
update_bpm_button_y=400
update_peep_button_x=100
update_peep_button_y=500
startup="no"


class CustomScale(ttk.Scale):
    def __init__(self, master=None, **kw):
        self.variable = kw.pop('variable', DoubleVar(master))
        ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
        self._style_name = '{}.custom.Horizontal.TScale'.format(self) # unique style name to handle the text
        self['style'] = self._style_name
        self.variable.trace_add('write', self._update_text)
        self._update_text()
    def _update_text(self, *args):
        global scaling
        global scale_value
        global scale_label
        global property_being_updated
        global value_pressure
        global value_vol
        global value_bpm
        global value_peep
        scale_value.place_forget()
        scale_label.place_forget()
        if property_being_updated=="Pressure":
            value_pressure=format(int(self.variable.get()))
        if property_being_updated=="Tidal Volume":
            value_vol=format(int(self.variable.get()))
        if property_being_updated=="BPM":
            value_bpm=format(int(self.variable.get()))
        if property_being_updated=="PEEP":
            value_peep=format(int(self.variable.get()))
        scale_value=Label(window, text=str(int(self.variable.get())), bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        if scaling=="yes":
            scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
            scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
        #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))

window = Tk()
window.title("Ventilator")
window.geometry("1024x768+0+0")
window.configure(background="black")

def create_ventilation_scales():
    global scale_vol
    global scale_pressure
    global scale_bpm
    global scale_peep
    global scale_oxygen
    scale_vol= CustomScale(window, from_=0, to=35)
    scale_pressure = CustomScale(window, from_=0, to=100)
    scale_bpm = CustomScale(window, from_=0, to=100)
    scale_peep = CustomScale(window, from_=0, to=100)

def update_peep():
    hide_user_entered_buttons()
    global scaling
    global property_being_updated
    global value_peep
    global scale_value
    global scale_label
    global scale_unit_label
    cross_button.place(x=cross_location_x,y=cross_location_y)
    tick_button.place(x=tick_location_x,y=tick_location_y)
    property_being_updated="PEEP"
    unit_of_property_being_updated="mmH20"
    scaling="yes"
    scale_value=Label(window, text=value_peep, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
    scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
    scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
    scale_peep.place(x=scale_location_x,y=scale_location_y)
    scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
    scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
    scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)
update_peep_button_image=PhotoImage(file="update_peep.gif")
update_peep_image_properties=Label(window, image=update_peep_button_image, bg="black")
update_peep_button=Button(window, image=update_peep_button_image, highlightthickness=0,bd=0,bg="white",command=update_peep)
update_peep_button.place(x=update_peep_button_x,y=update_peep_button_y)

def update_bpm():
    hide_user_entered_buttons()
    global scaling
    global property_being_updated
    global value_bpm
    global scale_value
    global scale_label
    global scale_unit_label
    cross_button.place(x=cross_location_x,y=cross_location_y)
    tick_button.place(x=tick_location_x,y=tick_location_y)
    property_being_updated="BPM"
    unit_of_property_being_updated=""
    scaling="yes"
    scale_value=Label(window, text=value_bpm, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
    scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
    scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
    scale_bpm.place(x=scale_location_x,y=scale_location_y)
    scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
    scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
    scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)
update_bpm_button_image=PhotoImage(file="update_bpm.gif")
update_bpm_button=Button(window, image=update_bpm_button_image, highlightthickness=0,bd=0,bg="white",command=update_bpm)
update_bpm_button.place(x=update_bpm_button_x,y=update_bpm_button_y)

def update_volume():
    hide_user_entered_buttons()
    global scaling
    global property_being_updated
    global value_vol
    global scale_value
    global scale_label
    global scale_unit_label
    cross_button.place(x=cross_location_x,y=cross_location_y)
    tick_button.place(x=tick_location_x,y=tick_location_y)
    property_being_updated="Tidal Volume"
    unit_of_property_being_updated="mL"
    scaling="yes"
    scale_value=Label(window, text=value_vol, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
    scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
    scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
    scale_vol.place(x=scale_location_x,y=scale_location_y)
    scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
    scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
    scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)
update_vol_button_image=PhotoImage(file="update_vol.gif")
update_vol_button=Button(window, image=update_vol_button_image, highlightthickness=0,bd=0,bg="white",command=update_volume)
update_vol_button.place(x=update_vol_button_x,y=update_vol_button_y)

def update_pressure():
    hide_user_entered_buttons()
    global scaling
    global property_being_updated
    global value_pressure
    global scale_value
    global scale_label
    global scale_unit_label
    cross_button.place(x=cross_location_x,y=cross_location_y)
    tick_button.place(x=tick_location_x,y=tick_location_y)
    property_being_updated="Pressure"
    unit_of_property_being_updated="mmH20"
    scaling="yes"
    scale_value=Label(window, text=value_pressure, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
    scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
    scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
    scale_pressure.place(x=scale_location_x,y=scale_location_y)
    scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
    scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
    scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)
update_pressure_button_image=PhotoImage(file="update_p.gif")
update_pressure_button=Button(window, image=update_pressure_button_image, highlightthickness=0,bd=0,bg="white",command=update_pressure)
update_pressure_button.place(x=update_pressure_button_x,y=update_pressure_button_y)

def cancel_sclaing():
    global scale_value
    global scale_label
    global scale_unit_label
    hide_user_entered_buttons()
    hide_scale_bars()
    hide_numeric_display_for_scale()
    hide_tick_and_cross_buttons()
    place_user_entered_buttons()
cross_button_image=PhotoImage(file="cross.gif")
cross_button=Button(window, image=cross_button_image, highlightthickness=0,bd=0,bg="white",command=cancel_sclaing)

def hide_tick_and_cross_buttons():
    tick_button.place_forget()
    cross_button.place_forget()

def hide_scale_bars():
    scale_pressure.place_forget()
    scale_vol.place_forget()
    scale_bpm.place_forget()
    scale_peep.place_forget()

def hide_numeric_display_for_scale():
    scale_value.place_forget()
    scale_label.place_forget()
    scale_unit_label.place_forget()

def hide_user_entered_buttons():
    update_pressure_button.place_forget()
    update_vol_button.place_forget()
    update_bpm_button.place_forget()
    update_peep_button.place_forget()

def place_user_entered_buttons():
    update_pressure_button.place(x=update_pressure_button_x,y=update_pressure_button_y)
    update_vol_button.place(x=update_vol_button_x,y=update_vol_button_y)
    update_bpm_button.place(x=update_bpm_button_x,y=update_bpm_button_y)
    update_peep_button.place(x=update_peep_button_x,y=update_peep_button_y)

def tick_pressed():
    global value_vol
    global value_pressure
    global value_bpm
    global value_peep
    global property_being_updated
    global startup
    print("tick",startup)
    create_style()
    place_user_entered_buttons()
    hide_numeric_display_for_scale()
    hide_scale_bars()
    hide_tick_and_cross_buttons()
    if property_being_updated=="Tidal Volume":
        send_value_to_sensor(property_being_updated,value_vol)
    if property_being_updated=="BPM":
        send_value_to_sensor(property_being_updated,value_bpm)
    if property_being_updated=="PEEP":
        send_value_to_sensor(property_being_updated,value_peep)
    if property_being_updated=="Pressure":
        send_value_to_sensor(property_being_updated,value_pressure)
    if startup=="no":
        startup="yes"
        return()
    if startup=="yes":
        startup="no"
        return()
tick_button_image=PhotoImage(file="tick.gif")
tick_image_properties=Label(window, image=tick_button_image, bg="black")
tick_button=Button(window, image=tick_button_image, highlightthickness=0,bd=0,bg="white",command=tick_pressed)

def send_value_to_sensor(property_being_updated,value):
    print(property_being_updated, value)
    print(startup)
window.mainloop()

from tkinter import *
from tkinter import ttk


scaling="not"
property_being_updated="none"
unit_of_property_being_updated="none"
value_pressure=0
value_vol=0
value_peep=0
value_bpm=0
value_oxygen=0


window = Tk()
window.title("Ventilator")
window.geometry("1024x768+0+0")
window.configure(background="black")

style = ttk.Style(window)

"""CLASS: MONITORED SYSTEM/START"""
class display_values_being_monitored():
    global y_increment_monitored_values_block
    y_increment_monitored_values_block=100
    def display_Peak_Pressure(Peak_Pressure,max,min):
        global Peak_P_number
        global Peak_P_label
        global Peak_P_unit
        global Peak_P_maximum
        global Peak_P_minimum
        line_number=1
        line=line_number-1
        x_increment=0; y_increment=65
        Peak_P_number=Label(window, text=Peak_Pressure, bg="black", fg="white",font=("montserrat",34,"normal"))
        Peak_P_label=Label(window, text="Peak Pressure", bg="black", fg="white",font=("montserrat light",12,"normal"))
        Peak_P_unit=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",12,"normal"))
        Peak_P_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
        Peak_P_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
        Peak_P_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
        Peak_P_label.place(x=185,y=y_increment_monitored_values_block+47+line*y_increment)
        Peak_P_unit.place(x=185+x_increment,y=y_increment_monitored_values_block+68+line*y_increment)
        Peak_P_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
        Peak_P_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

    def display_BPM(BPM,max,min):
        global BPM_number
        global BPM_label
        global BPM_unit
        global BPM_maximum
        global BPM_minimum
        line_number=2
        line=line_number-1
        x_increment=0; y_increment=65
        BPM_number=Label(window, text=BPM, bg="black", fg="white",font=("montserrat",34,"normal"))
        BPM_label=Label(window, text="BPM", bg="black", fg="white",font=("montserrat light",12,"normal"))
        BPM_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
        BPM_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
        BPM_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
        BPM_label.place(x=185+x_increment,y=y_increment_monitored_values_block+47+line*y_increment)
        BPM_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
        BPM_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

    def display_Flow(Flow,max,min):
        global flow_number
        global flow_label
        global flow_unit
        global flow_maximum
        global flow_minimum
        line_number=3
        line=line_number-1
        x_increment=0; y_increment=65
        flow_number=Label(window, text=Flow, bg="black", fg="white",font=("montserrat",34,"normal"))
        flow_label=Label(window, text="Flow", bg="black", fg="white",font=("montserrat light",12,"normal"))
        flow_unit=Label(window, text="L/min", bg="black", fg="white",font=("montserrat light",12,"normal"))
        flow_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
        flow_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
        flow_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
        flow_label.place(x=185+x_increment,y=y_increment_monitored_values_block+47+y_increment)
        flow_unit.place(x=185+x_increment,y=y_increment_monitored_values_block+68+line*y_increment)
        flow_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
        flow_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

    def display_VTE(VTE,max,min):
        global VTE_number
        global VTE_label
        global VTE_unit
        global VTE_maximum
        global VTE_minimum
        line_number=4
        line=line_number-1
        x_increment=0; y_increment=65
        VTE_number=Label(window, text=VTE, bg="black", fg="white",font=("montserrat",34,"normal"))
        VTE_label=Label(window, text="VTE", bg="black", fg="white",font=("montserrat light",12,"normal"))
        VTE_unit=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",12,"normal"))
        VTE_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
        VTE_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
        VTE_number.place(x=90+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
        VTE_label.place(x=185+x_increment,y=y_increment_monitored_values_block+47+line*y_increment)
        VTE_unit.place(x=185+x_increment,y=y_increment_monitored_values_block+68+line*y_increment)
        VTE_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
        VTE_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

    def display_IE(IE,max,min):
        global IE_number
        global IE_label
        global IE_unit
        global IE_maximum
        global IE_minimum
        line_number=5
        line=line_number-1
        x_increment=0; y_increment=65
        IE_number=Label(window, text="1:"+str(IE), bg="black", fg="white",font=("montserrat",34,"normal"))
        IE_label=Label(window, text="IE Ratio", bg="black", fg="white",font=("montserrat light",12,"normal"))
        IE_maximum=Label(window, text="1:"+str(max), bg="black", fg="white",font=("montserrat light",10,"normal"))
        IE_minimum=Label(window, text="1:"+str(min), bg="black", fg="white",font=("montserrat light",10,"normal"))
        IE_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
        IE_label.place(x=185+x_increment,y=y_increment_monitored_values_block+47+line*y_increment)
        IE_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
        IE_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

    def display_monitored_values():
        display_values_being_monitored.display_Peak_Pressure(35,32,2)
        display_values_being_monitored.display_BPM(21,32,2)
        display_values_being_monitored.display_Flow(8.1,32,2)
        display_values_being_monitored.display_VTE(900,1400,500)
        display_values_being_monitored.display_IE(2,1.5,1.25)

    def hide_monitored_values():
        global Peak_P_number
        global Peak_P_label
        global Peak_P_unit
        global Peak_P_maximum
        global Peak_P_minimum
        Peak_P_number.place_forget()
        Peak_P_label.place_forget()
        Peak_P_unit.place_forget()
        Peak_P_maximum.place_forget()
        Peak_P_minimum.place_forget()
        global BPM_number
        global BPM_label
        global BPM_unit
        global BPM_maximum
        global BPM_minimum
        BPM_number.place_forget()
        BPM_label.place_forget()
        BPM_maximum.place_forget()
        BPM_minimum.place_forget()
        global flow_number
        global flow_label
        global flow_unit
        global flow_maximum
        global flow_minimum
        flow_number.place_forget()
        flow_label.place_forget()
        flow_unit.place_forget()
        flow_maximum.place_forget()
        flow_minimum.place_forget()
        global VTE_number
        global VTE_label
        global VTE_unit
        global VTE_maximum
        global VTE_minimum
        VTE_number.place_forget()
        VTE_label.place_forget()
        VTE_unit.place_forget()
        VTE_maximum.place_forget()
        VTE_minimum.place_forget()
        global IE_number
        global IE_label
        global IE_unit
        global IE_maximum
        global IE_minimum
        IE_number.place_forget()
        IE_label.place_forget()
        IE_maximum.place_forget()
        IE_minimum.place_forget()
"""CLASS: MONITORED SYSTEM/END"""

"""CLASS: USER ENTERED SYSTEM/START"""

class ventilation_updating():
    global scale_value
    global scale_label
    global scale_unit_label
    scale_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
    scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
    global CustomScale
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

    def create_ventilation_bar_and_slider():
        global img_trough_ventilation
        global img_slider_ventilation
        img_trough_ventilation = PhotoImage(file="bar_small.gif")
        img_slider = PhotoImage(file="slider_small.gif")
    create_ventilation_bar_and_slider()

    def create_style_for_ventilation():
        global img_trough_ventilation
        global img_slider_ventilation
        img_trough_ventilation = PhotoImage(file="bar.gif")
        img_slider_ventilation = PhotoImage(file="slider.gif")
        # create scale elements
        string_ventilation_trough='.custom.Horizontal.Scale.trough'
        string_ventilation_slider='.custom.Horizontal.Scale.slider'
        style.element_create(string_ventilation_trough, 'image', img_trough_ventilation)
        style.element_create(string_ventilation_slider, 'image', img_slider_ventilation)
        # create custom layout
        style.layout('custom.Horizontal.TScale',[(string_ventilation_trough, {'sticky': 'ns'}),
                    (string_ventilation_slider, {'side': 'left', 'sticky': '','children': [('custom.Horizontal.Scale.label', {'sticky': ''})]})])
    create_style_for_ventilation()

    def create_ventilation_scales():
        global CustomScale
        global scale_vol
        global scale_pressure
        global scale_bpm
        global scale_peep
        global scale_oxygen
        scale_vol= CustomScale(window, from_=0, to=35)
        scale_pressure = CustomScale(window, from_=0, to=100)
        scale_bpm = CustomScale(window, from_=0, to=100)
        scale_peep = CustomScale(window, from_=0, to=100)
    create_ventilation_scales()
    global y_increment_update_buttons_block
    global scale_location_x
    global scale_location_y
    global unit_increment_y
    global value_increment_y
    global scale_label_location_x
    global scale_label_location_y
    global scale_value_location_x
    global scale_value_location_y
    global scale_value_unit_location_x
    global scale_value_unit_location_y
    global cross_location_x
    global cross_location_y
    global tick_location_x
    global tick_location_y
    y_increment_bottom_scale_block=600
    scale_location_x=300
    scale_location_y=10+y_increment_bottom_scale_block
    unit_increment_y=33
    value_increment_y=30
    scale_label_location_x=750
    scale_label_location_y=99+y_increment_bottom_scale_block
    scale_value_location_x=752
    scale_value_location_y=scale_label_location_y+value_increment_y
    scale_value_unit_location_x=750
    scale_value_unit_location_y=scale_value_location_y+unit_increment_y
    cross_location_x=200
    cross_location_y=30+y_increment_bottom_scale_block
    tick_location_x=cross_location_x+1100
    tick_location_y=cross_location_y
    def update_peep():
        ventilation_updating.hide_user_entered_buttons()
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

    def update_bpm():
        ventilation_updating.hide_user_entered_buttons()
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

    def update_volume():
        ventilation_updating.hide_user_entered_buttons()
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

    def update_pressure():
        ventilation_updating.hide_user_entered_buttons()
        global cross_button
        global tick_button
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

    global update_peep_button
    global update_bpm_button
    global update_vol_button
    global update_pressure_button
    update_peep_button_image=PhotoImage(file="update_peep.gif")
    update_peep_button=Button(window, image=update_peep_button_image, highlightthickness=0,bd=0,bg="white",command=update_peep)
    update_bpm_button_image=PhotoImage(file="update_bpm.gif")
    update_bpm_button=Button(window, image=update_bpm_button_image, highlightthickness=0,bd=0,bg="white",command=update_bpm)
    update_vol_button_image=PhotoImage(file="update_vol.gif")
    update_vol_button=Button(window, image=update_vol_button_image, highlightthickness=0,bd=0,bg="white",command=update_volume)
    update_pressure_button_image=PhotoImage(file="update_p.gif")
    update_pressure_button=Button(window, image=update_pressure_button_image, highlightthickness=0,bd=0,bg="white",command=update_pressure)

    def place_user_entered_buttons():
        global update_peep_button
        global update_bpm_button
        global update_vol_button
        global update_pressure_button
        y_increment_monitored_values_block=100
        x_increment=0; y_increment=100
        line_1_x=1400
        line_1_y=50+y_increment_monitored_values_block
        line_number=1
        line=line_number-1
        update_pressure_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        line_number=2
        line=line_number-1
        update_peep_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        line_number=3
        line=line_number-1
        update_bpm_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        line_number=4
        line=line_number-1
        update_vol_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
    def cross_pressed():
        global update_peep_button
        global update_bpm_button
        global update_vol_button
        global update_pressure_button
        global scale_value
        global scale_label
        global scale_unit_label
        ventilation_updating.hide_user_entered_buttons()
        ventilation_updating.hide_scale_bars()
        ventilation_updating.hide_numeric_display_for_scale()
        ventilation_updating.hide_tick_and_cross_buttons()
        ventilation_updating.place_user_entered_buttons()
    global cross_button
    cross_button_image=PhotoImage(file="cross.gif")
    cross_button=Button(window, image=cross_button_image, highlightthickness=0,bd=0,bg="white",command=cross_pressed)

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
        global update_peep_button
        global update_bpm_button
        global update_vol_button
        global update_pressure_button
        update_pressure_button.place_forget()
        update_vol_button.place_forget()
        update_bpm_button.place_forget()
        update_peep_button.place_forget()

    def send_value_to_sensor(property_being_updated,value):
        print(property_being_updated, value)

    def tick_pressed():
        global value_vol
        global value_pressure
        global value_bpm
        global value_peep
        global property_being_updated
        ventilation_updating.place_user_entered_buttons()
        ventilation_updating.hide_numeric_display_for_scale()
        ventilation_updating.hide_scale_bars()
        ventilation_updating.hide_tick_and_cross_buttons()
        if property_being_updated=="Tidal Volume":
            ventilation_updating.send_value_to_sensor(property_being_updated,value_vol)
        if property_being_updated=="BPM":
            ventilation_updating.send_value_to_sensor(property_being_updated,value_bpm)
        if property_being_updated=="PEEP":
            ventilation_updating.send_value_to_sensor(property_being_updated,value_peep)
        if property_being_updated=="Pressure":
            ventilation_updating.send_value_to_sensor(property_being_updated,value_pressure)
    global tick_button
    tick_button_image=PhotoImage(file="tick.gif")
    tick_button=Button(window, image=tick_button_image, highlightthickness=0,bd=0,bg="white",command=tick_pressed)
"""CLASS: USER ENTERED SYSTEM/END"""

def start_ventilating():
    ventilation_updating.place_user_entered_buttons()
    display_values_being_monitored.display_monitored_values()
start_ventilating()

window.mainloop()

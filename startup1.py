from tkinter import *
from tkinter import ttk
y_inc=600

scale_location_x=300
scale_location_y=10+y_inc
unit_increment_y=33
value_increment_y=30
scale_label_location_x=750
scale_label_location_y=99+y_inc
scale_value_location_x=752
scale_value_location_y=scale_label_location_y+value_increment_y
scale_value_unit_location_x=750
scale_value_unit_location_y=scale_value_location_y+unit_increment_y
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
        global property_being_updated1
        global property_being_updated2
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
            if scale_location_status=="bottom":
                scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
                scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
            if scale_location_status=="centered":
                global startup_scale_pressure_value
                global startup_scale_peep_value
                startup_scale_pressure_value.place_forget()
                startup_scale_peep_value.place_forget()
                counter_pressure=0
                if property_being_updated1=="Pressure":
                    if counter_pressure==0:
                        value_pressure=format(int(self.variable.get()))
                        startup_scale_pressure_value=Label(window, text=str(value_pressure), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                        startup_scale_pressure_value.place(x=scale_value_pressure_location_x,y=scale_value_pressure_location_y, anchor = CENTER)
                        print("updating P")

                if property_being_updated2=="PEEP":
                    value_peep=format(int(self.variable.get()))
                    startup_scale_peep_value=Label(window, text=str(value_peep), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_peep_value.place(x=scale_value_peep_location_x,y=scale_value_peep_location_y, anchor = CENTER)
                    print(value_peep)

                style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))

                #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))

window = Tk()
window.title("Ventilator")
window.geometry("1024x768+0+0")
window.configure(background="black")

scale_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
style = ttk.Style(window)
#style2 = tk.Style(window)
def create_img():
    global img_trough
    global img_slider
    img_trough = PhotoImage(file="bar_small.gif")
    img_slider = PhotoImage(file="slider_small.gif")
#create_img()
create_style_counter=1
def create_style():
    global img_trough
    global img_slider
    global create_style_counter
    img_trough = PhotoImage(file="bar.gif")
    img_slider = PhotoImage(file="slider.gif")
    # create scale elements
    string_trough=str(create_style_counter)+'.custom.Horizontal.Scale.trough'
    string_slider=str(create_style_counter)+'.custom.Horizontal.Scale.slider'
    style.element_create(string_trough, 'image', img_trough)
    style.element_create(string_slider, 'image', img_slider)
    # create custom layout
    style.layout('custom.Horizontal.TScale',[(string_trough, {'sticky': 'ns'}),
                (string_slider, {'side': 'left', 'sticky': '','children': [('custom.Horizontal.Scale.label', {'sticky': ''})]})])
create_style()

scale_vol= CustomScale(window, from_=0, to=35)
scale_pressure = CustomScale(window, from_=0, to=100)
scale_bpm = CustomScale(window, from_=0, to=100)
scale_peep = CustomScale(window, from_=0, to=100)
"""USER ENTERED SYSTEM/START"""

def update_peep():
    global scale_location_status
    scale_location_status="bottom"
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

def update_bpm():
    global scale_location_status
    scale_location_status="bottom"
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
update_bpm_image_properties=Label(window, image=update_bpm_button_image, bg="black")
update_bpm_button=Button(window, image=update_bpm_button_image, highlightthickness=0,bd=0,bg="white",command=update_bpm)

def update_volume():
    global scale_location_status
    scale_location_status="bottom"
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
update_vol_image_properties=Label(window, image=update_vol_button_image, bg="black")
update_vol_button=Button(window, image=update_vol_button_image, highlightthickness=0,bd=0,bg="white",command=update_volume)

def update_pressure():
    global scale_location_status
    scale_location_status="bottom"
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
update_pressure_image_properties=Label(window, image=update_pressure_button_image, bg="black")
update_pressure_button=Button(window, image=update_pressure_button_image, highlightthickness=0,bd=0,bg="white",command=update_pressure)



def place_user_entered_buttons():
    y_increment_entire_block=100
    x_increment=0; y_increment=100
    line_1_x=1400
    line_1_y=50+y_increment_entire_block
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
cross_image_properties=Label(window, image=cross_button_image, bg="black")
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


def send_value_to_sensor(property_being_updated,value):
    print(property_being_updated, value)

def tick_pressed():
    global value_vol
    global value_pressure
    global value_bpm
    global value_peep
    global property_being_updated
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
tick_button_image=PhotoImage(file="tick.gif")
tick_image_properties=Label(window, image=tick_button_image, bg="black")
tick_button=Button(window, image=tick_button_image, highlightthickness=0,bd=0,bg="white",command=tick_pressed)

"""USER ENTERED SYSTEM/END"""
def start_ventilating():
    #display_monitored_values()
    place_user_entered_buttons()
scale_value_pressure_location_x=0
scale_value_pressure_location_y=0
scale_value_peep_location_x=0
scale_value_peep_location_y=0
property_being_updated1="n"
property_being_updated2="n"
startup_scale_pressure_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
startup_scale_peep_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
def place_everything_at_startup():
    global property_being_updated1
    global property_being_updated2
    # unit_increment_y=33
    # value_increment_y=30
    # scale_label_location_x=750
    # scale_label_location_y=99+y_inc
    # scale_value_location_x=752
    # scale_value_location_y=scale_label_location_y+value_increment_y
    # scale_value_unit_location_x=750
    # scale_value_unit_location_y=scale_value_location_y+unit_increment_y
    global scaling
    scaling="yes"
    global property_being_updated
    global scale_location_status


    scale_location_status="centered"
    y_increment_entire_block=100    # change this to move everything up or down
    line_1_y=50+y_increment_entire_block
    y_increment=100 #gap b/w lines
    y_unit_increment=30 #gap b/w property and unit
    y_display_increment=10
    line_1_x=100    # x location of line no.1. Since all labels are inclined verticaly. All have the same x_location. Change this to move everything horizontally
    x_increment=0
    x_scale_increment=120 #gap b/w label and scale
    x_display_increment=1200

    global value_pressure
    global scale_value
    global scale_label
    global scale_value_pressure_location_x
    global scale_value_pressure_location_y
    line_no=1
    line=line_no-1
    #label on the left
    property_being_updated1="Pressure"
    property_p_insp=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat",18,"normal"))
    unit_p_insp=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
    property_p_insp.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
    unit_p_insp.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
    #scale in the middle
    scale_pressure.place(x=line_1_x+x_increment+x_scale_increment,y=-13+line_1_y+line*y_increment)
    #values on the right
    startup_scale_pressure_value=Label(window, text=value_pressure, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
    scale_unit_label=Label(window, text="mmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
    scale_value_pressure_location_x=line_1_x+x_increment+x_display_increment
    scale_value_pressure_location_y=line_1_y+line*y_increment+y_display_increment
    startup_scale_pressure_value.place(x=scale_value_pressure_location_x,y=scale_value_pressure_location_y, anchor = CENTER)
    scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)


    global value_peep
    global scale_value_peep_location_x
    global scale_value_peep_location_y
    line_no=2
    line=line_no-1
    #label on the left
    property_being_updated2="PEEP"
    property_peep=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat",18,"normal"))
    unit_peep=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
    property_peep.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
    unit_peep.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
    #scale in the middle
    scale_peep.place(x=line_1_x+x_increment+x_scale_increment,y=-13+line_1_y+line*y_increment)
    #values on the right
    startup_scale_peep_value=Label(window, text=value_peep, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
    scale_unit_label=Label(window, text="mmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
    scale_value_peep_location_x=line_1_x+x_increment+x_display_increment
    scale_value_peep_location_y=line_1_y+line*y_increment+y_display_increment
    startup_scale_peep_value.place(x=scale_value_peep_location_x,y=scale_value_peep_location_y, anchor = CENTER)
    scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
    print("f ended")
def startup_protocol():
    place_everything_at_startup()
#start_ventilating()
startup_protocol()

window.mainloop()

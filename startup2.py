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

class CustomScale(ttk.Scale):
    def __init__(self, master=None, **kw):
        self.variable = kw.pop('variable', DoubleVar(master))
        ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
        self._style_name = 'pressure_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
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
            scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
            scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
        #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))

window = Tk()
window.title("Ventilator")
window.geometry("1024x768+0+0")
window.configure(background="black")
style = ttk.Style(window)



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

class startup():
    global packed_bpm
    global packed_vol
    global packed_peep
    global packed_oxygen
    global packed_pressure
    packed_bpm="packed bpm"
    packed_vol="packed vol"
    packed_peep="packed peep"
    packed_oxygen="packed oxygen"
    packed_pressure="packed pressure"
    global CustomScale_vol
    global CustomScale_bpm
    global CustomScale_peep
    global CustomScale_peep
    global CustomScale_oxygen
    global CustomScale_pressure
    class CustomScale_oxygen(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'oxygen_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global value_oxygen
            global packed_oxygen
            if scaling=="yes":
                if scale_location_status=="centered":
                    global startup_scale_oxygen_value
                    startup_scale_oxygen_value.place_forget()
                    value_oxygen=format(int(self.variable.get()))
                    startup_scale_oxygen_value=Label(window, text=str(value_oxygen), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_oxygen_value.place(x=scale_value_oxygen_location_x,y=scale_value_oxygen_location_y, anchor = CENTER)
                    packed_oxygen="Oxygen"+","+str(value_oxygen)+","
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))

    class CustomScale_vol(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'vol_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global value_vol
            global packed_vol
            if scaling=="yes":
                if scale_location_status=="centered":
                    global startup_scale_vol_value
                    startup_scale_vol_value.place_forget()
                    value_vol=format(int(self.variable.get()))
                    startup_scale_vol_value=Label(window, text=str(value_vol), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_vol_value.place(x=scale_value_vol_location_x,y=scale_value_vol_location_y, anchor = CENTER)
                    packed_vol="vol"+","+str(value_vol)+","
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))

    class CustomScale_bpm(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'bpm_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global value_bpm
            global packed_bpm
            if scaling=="yes":
                if scale_location_status=="centered":
                    global startup_scale_bpm_value
                    startup_scale_bpm_value.place_forget()
                    value_bpm=format(int(self.variable.get()))
                    startup_scale_bpm_value=Label(window, text=str(value_bpm), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_bpm_value.place(x=scale_value_bpm_location_x,y=scale_value_bpm_location_y, anchor = CENTER)
                    packed_bpm="bpm"+","+str(value_bpm)+","
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))

    class CustomScale_peep(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'peep_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global value_peep
            global packed_peep
            if scaling=="yes":
                if scale_location_status=="centered":
                    global startup_scale_peep_value
                    startup_scale_peep_value.place_forget()
                    value_peep=format(int(self.variable.get()))
                    startup_scale_peep_value=Label(window, text=str(value_peep), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_peep_value.place(x=scale_value_peep_location_x,y=scale_value_peep_location_y, anchor = CENTER)
                    packed_peep="peep"+","+str(value_peep)+","
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))

    class CustomScale_pressure(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'pressure_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global value_pressure
            global packed_pressure
            if scaling=="yes":
                if scale_location_status=="centered":
                    global startup_scale_pressure_value
                    startup_scale_pressure_value.place_forget()
                    value_pressure=format(int(self.variable.get()))
                    startup_scale_pressure_value=Label(window, text=str(value_pressure), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_pressure_value.place(x=scale_value_pressure_location_x,y=scale_value_pressure_location_y, anchor = CENTER)
                    packed_pressure="pressure"+","+str(value_pressure)+","
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))
    def create_startup_bar_and_slider():
        global startup_img_trough
        global startup_img_slider
        startup_img_trough = PhotoImage(file="startup_bar.gif")
        startup_img_slider = PhotoImage(file="startup_slider.gif")
    create_startup_bar_and_slider()
    def create_scale_styles_for_startup():
        # create scale elements
        string_startup_trough='pressure_custom.Horizontal.Scale.trough'
        string_startup_slider='pressure_custom.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', startup_img_trough)
        style.element_create(string_startup_slider, 'image', startup_img_slider)
        # create custom layout
        style.layout('pressure_custom.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('pressure_custom.Horizontal.Scale.label', {'sticky': ''})]})])
        string_startup_trough='peep_custom.Horizontal.Scale.trough'
        string_startup_slider='peep_custom.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', startup_img_trough)
        style.element_create(string_startup_slider, 'image', startup_img_slider)
        # create custom layout
        style.layout('peep_custom.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('peep_custom.Horizontal.Scale.label', {'sticky': ''})]})])
        string_startup_trough='vol_custom.Horizontal.Scale.trough'
        string_startup_slider='vol_custom.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', startup_img_trough)
        style.element_create(string_startup_slider, 'image', startup_img_slider)
        # create custom layout
        style.layout('vol_custom.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('vol_custom.Horizontal.Scale.label', {'sticky': ''})]})])
        string_startup_trough='oxygen_custom.Horizontal.Scale.trough'
        string_startup_slider='oxygen_custom.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', startup_img_trough)
        style.element_create(string_startup_slider, 'image', startup_img_slider)
        # create custom layout
        style.layout('oxygen_custom.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('oxygen_custom.Horizontal.Scale.label', {'sticky': ''})]})])
        string_startup_trough='bpm_custom.Horizontal.Scale.trough'
        string_startup_slider='bpm_custom.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', startup_img_trough)
        style.element_create(string_startup_slider, 'image', startup_img_slider)
        # create custom layout
        style.layout('bpm_custom.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('bpm_custom.Horizontal.Scale.label', {'sticky': ''})]})])
    create_scale_styles_for_startup()
    def create_startup_scales():
        global scale_vol
        global scale_pressure
        global scale_bpm
        global scale_peep
        global scale_oxygen
        scale_vol= CustomScale_vol(window, from_=0, to=35)
        scale_pressure = CustomScale_pressure(window, from_=0, to=100)
        scale_bpm = CustomScale_bpm(window, from_=0, to=100)
        scale_peep = CustomScale_peep(window, from_=0, to=100)
        scale_oxygen = CustomScale_oxygen(window, from_=0, to=100)

    global scale_value_pressure_location_x
    global scale_value_pressure_location_y
    global scale_value_peep_location_x
    global scale_value_peep_location_y
    global scale_value_bpm_location_x
    global scale_value_bpm_location_y
    global scale_value_vol_location_x
    global scale_value_vol_location_y
    global scale_value_oxygen_location_x
    global scale_value_oxygen_location_y
    global startup_scale_pressure_value
    global startup_scale_peep_value
    global startup_scale_bpm_value
    global startup_scale_vol_value
    global startup_scale_oxygen_value
    scale_value_pressure_location_x=0
    scale_value_pressure_location_y=0
    scale_value_peep_location_x=0
    scale_value_peep_location_y=0
    scale_value_bpm_location_x=0
    scale_value_bpm_location_y=0
    scale_value_vol_location_x=0
    scale_value_vol_location_y=0
    scale_value_oxygen_location_x=0
    scale_value_oxygen_location_y=0
    startup_scale_pressure_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_peep_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_bpm_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_vol_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_oxygen_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))

    def place_startup_scales():
        global property_p_insp
        global unit_p_insp_left
        global scale_pressure
        global startup_scale_pressure_value
        global p_scale_unit_label
        global property_peep
        global unit_peep
        global scale_peep
        global startup_scale_peep_value
        global peep_scale_unit_label
        global property_bpm
        global scale_bpm
        global startup_scale_bpm_value
        global property_vol
        global unit_vol_left
        global scale_vol
        global startup_scale_vol_value
        global vol_scale_unit_label
        global property_oxygen
        global unit_oxygen_left
        global scale_oxygen
        global startup_scale_oxygen_value
        global oxygen_scale_unit_label

        global scaling
        scaling="yes"
        global property_being_updated
        global scale_location_status
        scale_location_status="centered"
        y_increment_entire_block=85    # change this to move everything up or down
        line_1_y=50+y_increment_entire_block
        y_increment=85 #gap b/w lines
        y_unit_increment=35 #gap b/w property and unit
        y_scale_increment=-1 #gap b/w everything else and the scale. Use this to move just the scales up and down
        y_display_increment=10
        line_1_x=100    # x location of line no.1. Since all labels are inclined verticaly. All have the same x_location. Change this to move everything horizontally
        x_increment=0   # use this to change things horizontally rather than editing the value of line_1_x
        x_scale_increment=175 #gap b/w label and scale
        x_display_increment=1250 # gap b/w scale and the display to the right side of the scale
        global value_pressure
        global scale_value_pressure_location_x
        global scale_value_pressure_location_y
        line_no=1
        line=line_no-1
        #label on the left
        #property_being_updated1="Pressure"
        property_p_insp=Label(window, text="Pressure", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_p_insp_left=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_p_insp.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_p_insp_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        #scale in the middle
        scale_pressure.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        #values on the right
        startup_scale_pressure_value=Label(window, text=value_pressure, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        p_scale_unit_label=Label(window, text="mmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_pressure_location_x=line_1_x+x_increment+x_display_increment
        scale_value_pressure_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_pressure_value.place(x=scale_value_pressure_location_x,y=scale_value_pressure_location_y, anchor = CENTER)
        p_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        global value_peep
        global scale_value_peep_location_x
        global scale_value_peep_location_y
        line_no=2
        line=line_no-1
        property_peep=Label(window, text="PEEP", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_peep=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_peep.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_peep.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        #scale in the middle
        scale_peep.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        #values on the right
        startup_scale_peep_value=Label(window, text=value_peep, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        peep_scale_unit_label=Label(window, text="mmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_peep_location_x=line_1_x+x_increment+x_display_increment
        scale_value_peep_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_peep_value.place(x=scale_value_peep_location_x,y=scale_value_peep_location_y, anchor = CENTER)
        peep_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        global value_bpm
        global scale_value_bpm_location_x
        global scale_value_bpm_location_y
        line_no=3
        line=line_no-1
        property_bpm=Label(window, text="BPM", bg="black", fg="white",font=("montserrat",18,"normal"))
        property_bpm.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        scale_bpm.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        startup_scale_bpm_value=Label(window, text=value_bpm, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        scale_value_bpm_location_x=line_1_x+x_increment+x_display_increment
        scale_value_bpm_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_bpm_value.place(x=scale_value_bpm_location_x,y=scale_value_bpm_location_y, anchor = CENTER)
        global value_vol
        global scale_value_vol_location_x
        global scale_value_vol_location_y
        line_no=4
        line=line_no-1
        property_vol=Label(window, text="Tidal Volume", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_vol_left=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_vol.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_vol_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        scale_vol.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        startup_scale_vol_value=Label(window, text=value_vol, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        vol_scale_unit_label=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_vol_location_x=line_1_x+x_increment+x_display_increment
        scale_value_vol_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_vol_value.place(x=scale_value_vol_location_x,y=scale_value_vol_location_y, anchor = CENTER)
        vol_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        global value_oxygen
        global scale_value_oxygen_location_x
        global scale_value_oxygen_location_y
        line_no=5
        line=line_no-1
        property_oxygen=Label(window, text="Oxygen", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_oxygen_left=Label(window, text="%", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_oxygen.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_oxygen_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        scale_oxygen.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        startup_scale_oxygen_value=Label(window, text=value_oxygen, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        oxygen_scale_unit_label=Label(window, text="%", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_oxygen_location_x=line_1_x+x_increment+x_display_increment
        scale_value_oxygen_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_oxygen_value.place(x=scale_value_oxygen_location_x,y=scale_value_oxygen_location_y, anchor = CENTER)
        oxygen_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)

    def hide_the_scales_in_startup():
        global property_p_insp
        global unit_p_insp_left
        global scale_pressure
        global startup_scale_pressure_value
        global p_scale_unit_label
        global property_peep
        global unit_peep
        global scale_peep
        global startup_scale_peep_value
        global peep_scale_unit_label
        global property_bpm
        global scale_bpm
        global startup_scale_bpm_value
        global property_vol
        global unit_vol_left
        global scale_vol
        global startup_scale_vol_value
        global vol_scale_unit_label
        global property_oxygen
        global unit_oxygen_left
        global scale_oxygen
        global startup_scale_oxygen_value
        global oxygen_scale_unit_label
        property_p_insp.place_forget()
        unit_p_insp_left.place_forget()
        scale_pressure.place_forget()
        startup_scale_pressure_value.place_forget()
        p_scale_unit_label.place_forget()
        property_peep.place_forget()
        unit_peep.place_forget()
        scale_peep.place_forget()
        startup_scale_peep_value.place_forget()
        peep_scale_unit_label.place_forget()
        property_bpm.place_forget()
        scale_bpm.place_forget()
        startup_scale_bpm_value.place_forget()
        property_vol.place_forget()
        unit_vol_left.place_forget()
        scale_vol.place_forget()
        startup_scale_vol_value.place_forget()
        vol_scale_unit_label.place_forget()
        property_oxygen.place_forget()
        unit_oxygen_left.place_forget()
        scale_oxygen.place_forget()
        startup_scale_oxygen_value.place_forget()
        oxygen_scale_unit_label.place_forget()

    def start_ventilating():
        asddas=""
        send_value_to_sensor(asddas,packed_bpm)
        send_value_to_sensor(asddas,packed_vol)
        send_value_to_sensor(asddas,packed_peep)
        send_value_to_sensor(asddas,packed_pressure)
        send_value_to_sensor(asddas,packed_oxygen)
        #print(property_being_updated, value)
        #print("Startup ventilating function")
    def test_ventilation():
        startup.hide_the_scales_in_startup()
        print("Startup testing function")
    global next_startup_button
    global test_startup_button
    next_startup_button_image=PhotoImage(file="next.gif")
    next_startup_button=Button(window, image=next_startup_button_image, highlightthickness=0,bd=0,bg="white",command=start_ventilating)
    test_startup_button_image=PhotoImage(file="test.gif")
    test_startup_button=Button(window, image=test_startup_button_image, highlightthickness=0,bd=0,bg="white",command=test_ventilation)
    def place_startup_buttons():
        test_startup_x_location=750
        test_startup_y_location=675
        gap_between_buttons=-150
        next_startup_x_location=test_startup_x_location+gap_between_buttons
        next_startup_y_location=test_startup_y_location
        global next_startup_button
        global test_startup_button
        next_startup_button.place(x=test_startup_x_location,y=test_startup_y_location)
        test_startup_button.place(x=next_startup_x_location,y=next_startup_y_location)
    def startup_protocol():
        startup.create_startup_scales()
        startup.place_startup_scales()
        startup.place_startup_buttons()


def send_value_to_sensor(property_being_updated,value):
    print(property_being_updated, value)
#start_ventilating()
startup.startup_protocol()

window.mainloop()

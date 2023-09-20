from tkinter import *
from tkinter import ttk
import sys
sys.setrecursionlimit(100000000)
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
update=5
x=0
def get_from_scale(x):
    print(x)
counter=0
class CustomScale_pressure(ttk.Scale):
    def __init__(self, master=None, **kw):
        global update
        global counter
        self.variable_pressure = kw.pop('variable_pressure', DoubleVar(master))
        ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable_pressure, **kw)
        self.style1 = 'pressure_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
        self['style'] = self.style1
        self.variable_pressure.trace_add('write', self._update_text)

        #print("updating text with var1")
        self._update_text()

    def _update_text(self, *args):
        global scaling
        global scale_value
        global scale_label
        global value_peep

        #print("no loop")
        text="{:.1f}".format(int(self.variable_pressure.get()))
        print("text",text)


class CustomScale_peep(ttk.Scale):
    def __init__(self, master=None, **kw):
        global update
        global counter


        self.variable_peep = kw.pop('variable_peep', DoubleVar(master))
        ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable_peep, **kw)
        self.style2 = 'peep_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
        self['style'] = self.style2
        self.variable_peep.trace_add('write', self._update_text)
        #print("updated")
        update=1
        #print("updating text with var2")
        self._update_text()

    def _update_text(self, *args):
        global scaling
        global scale_value
        global scale_label
        global property_being_updated
        global value_peep
        global startup_scale_peep_value
        startup_scale_peep_value.place_forget()
        value_peep=format(int(self.variable_peep.get()))
        startup_scale_peep_value=Label(window, text=str(value_peep), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        startup_scale_peep_value.place(x=scale_value_peep_location_x,y=scale_value_peep_location_y, anchor = CENTER)


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
img_trough = PhotoImage(file="bar.gif")
img_slider = PhotoImage(file="slider.gif")
create_style_counter=1
def create_style():
    #global img_trough
    #global img_slider
    global create_style_counter
    #img_trough = PhotoImage(file="bar.gif")
    #img_slider = PhotoImage(file="slider.gif")
    # create scale elements
    string_trough='pressure_custom.Horizontal.Scale.trough'
    string_slider='pressure_custom.Horizontal.Scale.slider'
    style.element_create(string_trough, 'image', img_trough)
    style.element_create(string_slider, 'image', img_slider)
    # create custom layout
    style.layout('pressure_custom.Horizontal.TScale',[(string_trough, {'sticky': 'ns'}),
                (string_slider, {'side': 'left', 'sticky': '','children': [('pressure_custom.Horizontal.Scale.label', {'sticky': ''})]})])

    string_trough='peep_custom.Horizontal.Scale.trough'
    string_slider='peep_custom.Horizontal.Scale.slider'
    style.element_create(string_trough, 'image', img_trough)
    style.element_create(string_slider, 'image', img_slider)
    # create custom layout
    style.layout('peep_custom.Horizontal.TScale',[(string_trough, {'sticky': 'ns'}),
                (string_slider, {'side': 'left', 'sticky': '','children': [('peep_custom.Horizontal.Scale.label', {'sticky': ''})]})])

create_style()



"""if ban==1:
    scale_pressure = CustomScale_pressure(window, from_=0, to=100)
    ban=2
    scale_pressure.place(x=50,y=100)


if ban==2:
    create_style()
    scale_peep = CustomScale_peep(window, from_=0, to=100)
    scale_peep.place(x=50,y=250)"""


scale_value_pressure_location_x=0
scale_value_pressure_location_y=0
scale_value_peep_location_x=0
scale_value_peep_location_y=0
property_being_updated1="n"
property_being_updated2="n"
startup_scale_pressure_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
startup_scale_peep_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
scale_pressure = CustomScale_pressure(window, from_=0, to=100)
#scale_pressure.place(x=50,y=100)
scale_peep = CustomScale_peep(window, from_=0, to=100)
#scale_peep.place(x=50,y=250)
def place_everything_at_startup():
    global property_being_updated1
    global property_being_updated2
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
    print(x)
    return()

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
    get_from_scale(x)
#start_ventilating()
startup_protocol()

window.mainloop()

import struct
import time
import sys
import random
import serial
from tkinter import *
from tkinter import ttk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt


window = Tk()
window.title("Ventilator")
window.geometry("1024x768+0+0")
window.configure(background="black")


#stepper_data1=serial.Serial('COM7',baudrate=9600)
#time.sleep(0.5)

#An image of the EDM schematic

lungs_image_file=PhotoImage(file="lungs.gif")
lungs_image=Label (window, image=lungs_image_file, bg="black")
lungs_image.place(x=850,y=40)

Logo_header=PhotoImage(file="logo.gif")
Logo_header_properties=Label(window,image=Logo_header,bg="black")
Logo_header_properties.place(x=650,y=25)

Display_lungs_image=PhotoImage(file="lungs1.gif")
Display_lungs_image_properties=Label(window,image=Display_lungs_image,bg="black")
Display_lungs_image_properties.place(x=35,y=25)

BPM_entry_counter=0
def enter_BPM():
    global display_BPM
    global BPM_entry_counter
    BPM_value=int(BPM.get())
    upper_limit_BPM_value=int(upper_limit_BPM.get())
    lower_limit_BPM_value=int(lower_limit_BPM.get())
    x_coor=200;y_coor=50
    if BPM_entry_counter>0:
        display_BPM.place_forget()
    if lower_limit_BPM_value<=BPM_value<=upper_limit_BPM_value:
        displayed_string_BPM= str(BPM_value) + " Breaths Per Minute"
        display_BPM=Label(window, text=(displayed_string_BPM),bg="black", fg="white", font=("montserrat",14,"normal"))
        display_BPM.place(x=x_coor,y=y_coor)
        BPM_entry_counter=BPM_entry_counter+1
        #send_BPM_to_arduino()
    if BPM_value>upper_limit_BPM_value:
        display_BPM=Label(window, text=("o bhai banda ventilator par hai cycle par nai"),bg="black", fg="white", font=("montserrat",14,"normal"))
        display_BPM.place(x=x_coor,y=y_coor)
        BPM_entry_counter=BPM_entry_counter+1
    if BPM_value<lower_limit_BPM_value:
        display_BPM=Label(window, text=("haan agla toh pro swimmer hai na"),bg="black", fg="white", font=("montserrat",14,"normal"))
        BPM_entry_counter=BPM_entry_counter+1
        display_BPM.place(x=x_coor,y=y_coor)
BPM=StringVar()
lower_limit_BPM=StringVar(); upper_limit_BPM=StringVar()
lower_limit_BPM_entry=Entry(window,textvariable=lower_limit_BPM,width=5,bg="white")
upper_limit_BPM_entry=Entry(window,textvariable=upper_limit_BPM,width=5,bg="white")
lower_limit_BPM_entry.place(x=400,y=200)
upper_limit_BPM_entry.place(x=400+75,y=200)

Update_BPM=Button(window,text="Update BPM", font=("montserrat",10,"bold"), width=14, bg="white",fg="black",command=enter_BPM)
BPM_value_entry=Entry(window,textvariable=BPM,width=4,bg="white")
BPM_value_entry.place(x=150,y=205)

Update_BPM.place(x=200,y=202)
BPM_text=Label(window, text="BPM: ", bg="#262626", fg="white",font=("montserrat",14,"normal"))
BPM_text.place(x=30,y=200)

to_text_BPM=Label(window, text="to", bg="#262626", fg="white",font=("montserrat",14,"normal"))
to_text_BPM.place(x=442,y=195)
to_text_Pressure=Label(window, text="to", bg="#262626", fg="white",font=("montserrat",14,"normal"))
to_text_Pressure.place(x=442,y=195+35)
to_text_tidal_vol=Label(window, text="to", bg="#262626", fg="white",font=("montserrat",14,"normal"))
to_text_tidal_vol.place(x=442,y=195+35+35+35)

Pressure_entry_counter=0
def enter_Pressure():
    global display_Pressure
    global Pressure_entry_counter
    Pressure_value=int(Pressure.get())
    upper_limit_Pressure_value=int(upper_limit_Pressure.get())
    lower_limit_Pressure_value=int(lower_limit_Pressure.get())
    x_coor=200;y_coor=75
    if Pressure_entry_counter>0:
        display_Pressure.place_forget()
    if lower_limit_Pressure_value<=Pressure_value<=upper_limit_Pressure_value:
        displayed_string_Pressure= str(Pressure_value) + " mmH20"
        display_Pressure=Label(window, text=(displayed_string_Pressure),bg="#262626", fg="white", font=("montserrat",14,"normal"))
        display_Pressure.place(x=x_coor,y=y_coor)
        #send_BPM_to_arduino()
    if Pressure_value>upper_limit_Pressure_value:
        display_Pressure=Label(window, text=("banda phaarna ee?"),bg="#262626", fg="white", font=("montserrat",14,"normal"))
        display_Pressure.place(x=x_coor,y=y_coor)
    if Pressure_value<lower_limit_Pressure_value:
        display_Pressure=Label(window, text=("wesay hi gala daba do"),bg="#262626", fg="white", font=("montserrat",14,"normal"))
        display_Pressure.place(x=x_coor,y=y_coor)
    Pressure_entry_counter=Pressure_entry_counter+1
Pressure=StringVar()
lower_limit_Pressure=StringVar(); upper_limit_Pressure=StringVar()
lower_limit_Pressure_entry=Entry(window,textvariable=lower_limit_Pressure,width=5,bg="white")
upper_limit_Pressure_entry=Entry(window,textvariable=upper_limit_Pressure,width=5,bg="white")
lower_limit_Pressure_entry.place(x=400,y=200+35)
upper_limit_Pressure_entry.place(x=400+75,y=200+35)
Update_Pressure=Button(window,text="Update Pressure", font=("montserrat",10,"bold"), width=14, bg="white",fg="black",command=enter_Pressure)
Pressure_value_entry=Entry(window,textvariable=Pressure,width=4,bg="white")
Pressure_value_entry.place(x=150,y=205+35)
Update_Pressure.place(x=200,y=202+35)
Pressure_text=Label(window, text="Pressure: ", bg="#262626", fg="white",font=("montserrat",14,"normal"))
Pressure_text.place(x=30,y=200+35)

IE_ratio_counter=0
def enter_IE_ratio():
    global display_IE_ratio
    global IE_ratio_counter
    upper_limit_IE_ratio=35
    lower_limit_IE_ratio=29
    x_coor=200;y_coor=100
    if IE_ratio_counter>0:
        display_IE_ratio.place_forget()
    IE_ratio_value=float(IE.get())
    if lower_limit_IE_ratio<=IE_ratio_value<=upper_limit_IE_ratio:
        displayed_string_IE_ratio= str(IE_ratio_value) + " IE Ratio"
        display_IE_ratio=Label(window, text=(displayed_string_IE_ratio),bg="#262626", fg="white", font=("montserrat",14,"normal"))
        display_IE_ratio.place(x=x_coor,y=y_coor)
        #send_BPM_to_arduino()
    if IE_ratio_value>upper_limit_IE_ratio:
        display_IE_ratio=Label(window, text=("banda phaarna ee?"),bg="#262626", fg="white", font=("montserrat",14,"normal"))
        display_IE_ratio.place(x=x_coor,y=y_coor)
    if IE_ratio_value<lower_limit_IE_ratio:
        display_IE_ratio=Label(window, text=("wesay hi gala daba do"),bg="#262626", fg="white", font=("montserrat",14,"normal"))
        display_IE_ratio.place(x=x_coor,y=y_coor)
    IE_ratio_counter=IE_ratio_counter+1
IE=StringVar()
Update_IE_ratio=Button(window,text="Update IE ratio", font=("montserrat",10,"bold"), width=14, bg="white",fg="black",command=enter_IE_ratio)
IE_ratio_value_entry=Entry(window,textvariable=IE,width=4,bg="white")
IE_ratio_value_entry.place(x=150,y=205+35+35)
Update_IE_ratio.place(x=200,y=202+35+35)
IE_ratio_text=Label(window, text="IE Ratio: ", bg="#262626", fg="white",font=("montserrat",14,"normal"))
IE_ratio_text.place(x=30,y=200+35+35)

tidal_vol_counter=0
def enter_tidal_vol():
    global display_tidal_vol
    global tidal_vol_counter
    tidal_vol_value=int(tidal_vol.get())
    upper_limit_tidal_vol_value=int(upper_limit_tidal_vol.get())
    lower_limit_tidal_vol_value=int(lower_limit_tidal_vol.get())
    x_coor=200;y_coor=120+50
    if tidal_vol_counter>0:
        display_tidal_vol.place_forget()
    if lower_limit_tidal_vol_value<=tidal_vol_value<=upper_limit_tidal_vol_value:
        displayed_string_tidal_vol= str(tidal_vol_value) + " tidal vol"
        display_tidal_vol=Label(window, text=(displayed_string_tidal_vol),bg="#262626", fg="white", font=("montserrat",14,"normal"))
        display_tidal_vol.place(x=x_coor,y=y_coor)
        #send_BPM_to_arduino()
    if tidal_vol_value>upper_limit_tidal_vol_value:
        display_tidal_vol=Label(window, text=("banda phaarna ee?"),bg="#262626", fg="white", font=("montserrat",14,"normal"))
        display_tidal_vol.place(x=x_coor,y=y_coor)
    if tidal_vol_value<lower_limit_tidal_vol_value:
        displayed_tidal_vol=Label(window, text=("wesay hi gala daba do"),bg="#262626", fg="white", font=("montserrat",14,"normal"))
        displayed_tidal_vol.place(x=x_coor,y=y_coor)
    tidal_vol_counter=tidal_vol_counter+1
tidal_vol=StringVar()
lower_limit_tidal_vol=StringVar(); upper_limit_tidal_vol=StringVar()
lower_limit_tidal_vol_entry=Entry(window,textvariable=lower_limit_tidal_vol,width=5,bg="white")
upper_limit_tidal_vol_entry=Entry(window,textvariable=upper_limit_tidal_vol,width=5,bg="white")
lower_limit_tidal_vol_entry.place(x=400,y=200+35+35+35)
upper_limit_tidal_vol_entry.place(x=400+75,y=200+35+35+35)
Update_tidal_vol=Button(window,text="Update tidal vol", font=("montserrat",10,"bold"), width=14, bg="white",fg="black",command=enter_tidal_vol)
tidal_vol_value_entry=Entry(window,textvariable=tidal_vol,width=4,bg="white")
tidal_vol_value_entry.place(x=150,y=205+35+35+35)
Update_tidal_vol.place(x=200,y=202+35+35+35)
tidal_vol_text=Label(window, text="tidal vol: ", bg="#262626", fg="white",font=("montserrat",14,"normal"))
tidal_vol_text.place(x=30,y=200+35+35+35)

"""

plt.rcParams.update({'font.size': 10})
text_color = 'white'
plt.rcParams['text.color'] = text_color
plt.rcParams['axes.labelcolor'] = text_color
plt.rcParams['xtick.color'] = text_color
plt.rcParams['ytick.color'] = text_color
"""

plt.rcParams.update({'font.size': 10})
text_color = 'white'
plt.rcParams['text.color'] = text_color
plt.rcParams['axes.labelcolor'] = text_color
plt.rcParams['xtick.color'] = text_color
plt.rcParams['ytick.color'] = text_color
input_data_array=np.array([0])
x_axis_scale = np.array([0])
horizontal_axis=np.array([0])

loop_counter_pressure_graph=0
seconds_displayed=3
time_interval=0.1
data_points_displayed=seconds_displayed/time_interval
time_interval_millis=int(time_interval*1000)
def draw_pressure_graph():
    global input_data_array
    global x_axis_scale
    global horizontal_axis
    global loop_counter_pressure_graph
    if loop_counter_pressure_graph<data_points_displayed:
        x_axis_scale=np.append(x_axis_scale,[(loop_counter_pressure_graph+2)*time_interval])
        horizontal_axis=np.append(horizontal_axis,[0])
        if loop_counter_pressure_graph%2==0:
            print("even")
            input_data_array=np.append(input_data_array,[1])
        else:
            print("odd")
            input_data_array=np.append(input_data_array,[-1])
    if loop_counter_pressure_graph>=data_points_displayed:
        if loop_counter_pressure_graph%2==0:
            input_data_array=np.append(input_data_array,[1])
            input_data_array=np.delete(input_data_array, 0)
        else:
            input_data_array=np.append(input_data_array,[-1])
            input_data_array=np.delete(input_data_array, 0)
    fig=Figure(figsize=(7,2.3), dpi=100)
    ax = fig.add_subplot(111)
    line= ax.plot(x_axis_scale, input_data_array, color='white')
    x_axis_line= ax.plot(x_axis_scale, horizontal_axis, linewidth=0.75, dashes=[4, 2, 4, 2],color='white')
    ax.set_facecolor('xkcd:black')   #background color
    fig.patch.set_facecolor('xkcd:black')
    graph = FigureCanvasTkAgg(fig, master=window)
    global canvas
    if loop_counter_pressure_graph>0:
         canvas.place_forget()
    canvas = graph.get_tk_widget()
    canvas.place(x=0,y=10)
    loop_counter_pressure_graph=loop_counter_pressure_graph+1
    window.after(time_interval_millis, draw_pressure_graph)

draw_pressure_graph()

window.mainloop()

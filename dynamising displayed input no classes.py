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


loop_counter_pressure_graph=0
seconds_displayed=3
time_interval=0.1
data_points_displayed=seconds_displayed/time_interval
time_interval_millis=int(time_interval*1000)
input_data_array=np.array([0])
x_axis_scale = np.array([0])
horizontal_axis=np.array([0])
plt.rcParams.update({'font.size': 10})
text_color = 'white'
plt.rcParams['text.color'] = text_color
plt.rcParams['axes.labelcolor'] = text_color
plt.rcParams['xtick.color'] = text_color
plt.rcParams['ytick.color'] = text_color
def draw_pressure_graph(pressure_value):
    global input_data_array
    global x_axis_scale
    global horizontal_axis
    global loop_counter_pressure_graph
    if loop_counter_pressure_graph<data_points_displayed:
        x_axis_scale=np.append(x_axis_scale,[(loop_counter_pressure_graph+2)*time_interval])
        horizontal_axis=np.append(horizontal_axis,[0])
        input_data_array=np.append(input_data_array,[pressure_value])
    if loop_counter_pressure_graph>=data_points_displayed:
        input_data_array=np.append(input_data_array,[pressure_value])
        input_data_array=np.delete(input_data_array, 0)
    fig=Figure(figsize=(7,2.3), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_facecolor('xkcd:black')   #background color
    fig.patch.set_facecolor('xkcd:black')
    line= ax.plot(x_axis_scale, input_data_array, color='white')
    x_axis_line= ax.plot(x_axis_scale, horizontal_axis, linewidth=0.75, dashes=[4, 2, 4, 2],color='white')
    graph = FigureCanvasTkAgg(fig, master=window)
    global canvas
    if loop_counter_pressure_graph>0:
        canvas.place_forget()
    canvas = graph.get_tk_widget()
    canvas.place(x=0,y=10)
    loop_counter_pressure_graph=loop_counter_pressure_graph+1

input_data_array_flow=np.array([0])
x_axis_scale_flow = np.array([0])
horizontal_axis_flow=np.array([0])
loop_counter_flow_graph=0
seconds_displayed_flow=3
time_interval_flow=0.1
data_points_displayed_flow=seconds_displayed_flow/time_interval_flow
time_interval_millis_flow=int(time_interval_flow*1000)
plt.rcParams.update({'font.size': 10})
text_color = 'white'
plt.rcParams['text.color'] = text_color
plt.rcParams['axes.labelcolor'] = text_color
plt.rcParams['xtick.color'] = text_color
plt.rcParams['ytick.color'] = text_color
def draw_flow_graph(flow_value):
    flow_value_displayed=flow_value
    global input_data_array_flow
    global x_axis_scale_flow
    global horizontal_axis_flow
    global loop_counter_flow_graph
    if loop_counter_flow_graph<data_points_displayed_flow:
        x_axis_scale_flow=np.append(x_axis_scale_flow,[(loop_counter_flow_graph+2)*time_interval_flow])
        horizontal_axis_flow=np.append(horizontal_axis_flow,[0])
        input_data_array_flow=np.append(input_data_array_flow,[flow_value])
    if loop_counter_flow_graph>=data_points_displayed_flow:
        input_data_array_flow=np.append(input_data_array_flow,[flow_value])
        input_data_array_flow=np.delete(input_data_array_flow, 0)
    fig_flow=Figure(figsize=(7,2.3), dpi=100)
    ax_flow = fig_flow.add_subplot(111)
    line_flow= ax_flow.plot(x_axis_scale_flow, input_data_array_flow, color='white')
    x_axis_line_flow= ax_flow.plot(x_axis_scale_flow, horizontal_axis_flow, linewidth=0.75, dashes=[4, 2, 4, 2],color='white')
    ax_flow.set_facecolor('xkcd:black')   #background color
    fig_flow.patch.set_facecolor('xkcd:black')
    graph_flow = FigureCanvasTkAgg(fig_flow, master=window)
    global canvas_flow
    if loop_counter_flow_graph>0:
        canvas_flow.place_forget()
    canvas_flow = graph_flow.get_tk_widget()
    canvas_flow.place(x=0,y=500)
    loop_counter_flow_graph=loop_counter_flow_graph+1
def hide_all_graphs():
    global canvas_flow
    global canvas
    canvas_flow.place_forget()
    canvas.place_forget()

hide_the_graphs="no"
def call_graph():
    global hide_the_graphs
    draw_flow_graph(12)
    draw_pressure_graph(1)
    if hide_the_graphs=="no":
        # time_interval_millis
        window.after(time_interval_millis, call_graph)
counter_for_hiding_graphs=0     #this is defined so that the hide_graphs function would only run once. there is a window.after command used and without this counter, it could cause the hide_graphs to run indefinitely, again and again
def hide_graphs():
    global hide_the_graphs
    global counter_for_hiding_graphs
    hide_all_graphs()
    if hide_the_graphs=="no":
        counter_for_hiding_graphs=0
        if counter_for_hiding_graphs<1:
            hide_the_graphs="yes"
            window.after(time_interval_millis, hide_graphs)
    if counter_for_hiding_graphs>=1:
        print("counter exceeded")
        counter_for_hiding_graphs=0
        hide_the_graphs="no"
    counter_for_hiding_graphs=counter_for_hiding_graphs+1

quit_button_image=PhotoImage(file="tick.gif")
quit_button=Button(window, image=quit_button_image, highlightthickness=0,bd=0,bg="white",command=call_graph)
quit_button.place(x=799,y=50)

quit2_button_image=PhotoImage(file="cross.gif")
quit2_button=Button(window, image=quit2_button_image, highlightthickness=0,bd=0,bg="white",command=hide_graphs)
quit2_button.place(x=799,y=120)

"""
value_received=1
def data_grabber():
    global value_received
    value_received=value_received+1

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
display_Peak_Pressure(11,1,1)
"""
"""
input_data_array_flow=np.array([0])
x_axis_scale_flow = np.array([0])
horizontal_axis_flow=np.array([0])

loop_counter_flow_graph=0
seconds_displayed_flow=5
time_interval_flow=0.15
data_points_displayed_flow=seconds_displayed_flow/time_interval_flow
time_interval_millis_flow=int(time_interval_flow*1000)

def draw_flow_graph(flow_value):
    plt.rcParams.update({'font.size': 10})
    text_color = 'white'
    plt.rcParams['text.color'] = text_color
    plt.rcParams['axes.labelcolor'] = text_color
    plt.rcParams['xtick.color'] = text_color
    plt.rcParams['ytick.color'] = text_color
    flow_value_displayed=flow_value
    global input_data_array_flow
    global x_axis_scale_flow
    global horizontal_axis_flow
    global loop_counter_flow_graph
    if loop_counter_flow_graph<data_points_displayed_flow:
        x_axis_scale_flow=np.append(x_axis_scale_flow,[(loop_counter_flow_graph+2)*time_interval_flow])
        horizontal_axis_flow=np.append(horizontal_axis_flow,[0])
        input_data_array_flow=np.append(input_data_array_flow,[flow_value])
    if loop_counter_flow_graph>=data_points_displayed_flow:
        input_data_array_flow=np.append(input_data_array_flow,[flow_value])
        input_data_array_flow=np.delete(input_data_array_flow, 0)
    fig_flow=Figure(figsize=(7,2.3), dpi=100)
    ax_flow = fig_flow.add_subplot(111)
    line_flow= ax_flow.plot(x_axis_scale_flow, input_data_array_flow, color='white')
    dashes = [10, 5, 100, 5]
    x_axis_line_flow= ax_flow.plot(x_axis_scale_flow, horizontal_axis_flow, linewidth=0.75, dashes=[4, 2, 4, 2],color='white')
    ax_flow.set_facecolor('xkcd:black')   #background color
    fig_flow.patch.set_facecolor('xkcd:black')
    graph_flow = FigureCanvasTkAgg(fig_flow, master=window)
    canvas_flow = graph_flow.get_tk_widget()
    canvas_flow.place(x=0,y=500)
    loop_counter_flow_graph=loop_counter_flow_graph+1
"""


"""
input_data_array_flow=np.array([0])
x_axis_scale_flow = np.array([0])
horizontal_axis_flow=np.array([0])

loop_counter_flow_graph=0
seconds_displayed_flow=5
time_interval_flow=0.15
data_points_displayed_flow=seconds_displayed_flow/time_interval_flow
time_interval_millis_flow=int(time_interval_flow*1000)

def draw_flow_graph():
    global input_data_array_flow
    global x_axis_scale_flow
    global horizontal_axis_flow
    global loop_counter_flow_graph
    if loop_counter_flow_graph<data_points_displayed_flow:
        x_axis_scale_flow=np.append(x_axis_scale_flow,[(loop_counter_flow_graph+2)*time_interval_flow])
        horizontal_axis_flow=np.append(horizontal_axis_flow,[0])
        if loop_counter_flow_graph%2==0:
            print("flow even")
            input_data_array_flow=np.append(input_data_array_flow,[1])
        else:
            print("flow odd")
            input_data_array_flow=np.append(input_data_array_flow,[-1])
    if loop_counter_flow_graph>=data_points_displayed_flow:
        if loop_counter_flow_graph%2==0:
            input_data_array_flow=np.append(input_data_array_flow,[1])
            input_data_array_flow=np.delete(input_data_array_flow, 0)
        else:
            input_data_array_flow=np.append(input_data_array_flow,[-1])
            input_data_array_flow=np.delete(input_data_array_flow, 0)
    fig_flow=Figure(figsize=(7,2.3), dpi=100)
    ax_flow = fig_flow.add_subplot(111)
    line_flow= ax_flow.plot(x_axis_scale_flow, input_data_array_flow, color='white')
    dashes = [10, 5, 100, 5]
    x_axis_line_flow= ax_flow.plot(x_axis_scale_flow, horizontal_axis_flow, linewidth=0.75, dashes=[4, 2, 4, 2],color='white')
    ax_flow.set_facecolor('xkcd:black')   #background color
    fig_flow.patch.set_facecolor('xkcd:black')
    graph_flow = FigureCanvasTkAgg(fig_flow, master=window)
    canvas_flow = graph_flow.get_tk_widget()
    canvas_flow.place(x=0,y=500)
    loop_counter_flow_graph=loop_counter_flow_graph+1
    window.after(time_interval_millis_flow, draw_flow_graph)
draw_flow_graph()
"""


def monitoring_protocol():
    data_grabber()
    print()
window.mainloop()

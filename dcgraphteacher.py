from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


window = Tk()
window.title("Ventilator")
window.geometry("1024x768+0+0")
window.configure(background="black")

plt.rcParams.update({'font.size': 10})
text_color = 'white'
plt.rcParams['text.color'] = text_color
plt.rcParams['axes.labelcolor'] = text_color
plt.rcParams['xtick.color'] = text_color
plt.rcParams['ytick.color'] = text_color
global x_data_pressure
global y_data_pressure
global y_val_pressure
global starting_time_pressure
global time_interval_pressure
global total_time_pressure
global data_points_pressure
global animation_loop_counter_pressure
global array_character_number_being_printed
global data_points_in_one_array
x_data_pressure = np.array([0])
y_data_pressure = np.array([0])
starting_time_pressure=0
data_points_in_one_array=5
time_interval_pressure=0.1/data_points_in_one_array
total_time_pressure=5
data_points_pressure=total_time_pressure/time_interval_pressure
animation_loop_counter_pressure=0
value_pressure_received_1=5
def animation_frame_pressure(i):
    global time_interval_pressure
    global starting_time_pressure
    global y_val_pressure
    global x_data_pressure
    global y_data_pressure
    global animation_loop_counter_pressure
    global array_character_number_being_printed
    starting_time_pressure=starting_time_pressure+time_interval_pressure
    if animation_loop_counter_pressure<data_points_pressure:
        x_data_pressure=np.append(x_data_pressure,[starting_time_pressure])
        y_data_pressure=np.append(y_data_pressure,[value_pressure_received_1])
    if animation_loop_counter_pressure>=data_points_pressure:
        y_data_pressure=np.append(y_data_pressure,[value_pressure_received_1])
        y_data_pressure=np.delete(y_data_pressure,0)
    line_pressure.set_xdata(x_data_pressure)
    line_pressure.set_ydata(y_data_pressure)
    animation_loop_counter_pressure=animation_loop_counter_pressure+1
    return line_pressure,
global line_pressure
total_time_pressure=5
fig_pressure=Figure(figsize=(9,2.3), dpi=100)
ax_pressure = fig_pressure.add_subplot(111)
ax_pressure.set_facecolor('xkcd:black')   #background color
fig_pressure.patch.set_facecolor('xkcd:black')
ax_pressure.set_xlim(0, total_time_pressure)
ax_pressure.set_ylim(-2000, 2000)
line_pressure, = ax_pressure.plot(0, 0, color='white')
graph_pressure = FigureCanvasTkAgg(fig_pressure, master=window)
canvas_pressure=graph_pressure.get_tk_widget()
animation_pressure = FuncAnimation(fig_pressure, func=animation_frame_pressure, frames=1000, interval=time_interval_pressure*1000)
canvas_pressure.place(x=100,y=100)
window.mainloop()

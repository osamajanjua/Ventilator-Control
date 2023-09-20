from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 10})
text_color = 'white'
plt.rcParams['text.color'] = text_color
plt.rcParams['axes.labelcolor'] = text_color
plt.rcParams['xtick.color'] = text_color
plt.rcParams['ytick.color'] = text_color

input_data_array=np.array([0])
x_axis_scale = np.array([0])
horizontal_axis=np.array([0])

window = Tk()

loop_counter_pressure_graph=0
seconds_displayed=3
time_interval=0.10
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
    dashes = [10, 5, 100, 5]
    x_axis_line= ax.plot(x_axis_scale, horizontal_axis, linewidth=0.75, dashes=[4, 2, 4, 2],color='white')
    ax.set_facecolor('xkcd:black')   #background color
    fig.patch.set_facecolor('xkcd:black')
    graph = FigureCanvasTkAgg(fig, master=window)
    canvas = graph.get_tk_widget()
    canvas.place(x=0,y=10)
    loop_counter_pressure_graph=loop_counter_pressure_graph+1
    window.after(time_interval_millis, draw_pressure_graph)

draw_pressure_graph()
window.mainloop()

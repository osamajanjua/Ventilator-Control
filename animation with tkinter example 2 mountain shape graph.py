from tkinter import *
from tkinter import ttk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.rcParams.update({'font.size': 10})
text_color = 'white'
plt.rcParams['text.color'] = text_color
plt.rcParams['axes.labelcolor'] = text_color
plt.rcParams['xtick.color'] = text_color
plt.rcParams['ytick.color'] = text_color

window = Tk()
window.title("Ventilator")
window.geometry("1024x768+0+0")
window.configure(background="black")

x_data_pressure = np.array([0])
y_data_pressure = np.array([0])
y_val_pressure=5
starting_time_pressure=0
time_interval_pressure=0.1
def animation_frame_pressure(i):
	global time_interval_pressure
	global starting_time_pressure
	global y_val_pressure
	global x_data_pressure
	global y_data_pressure
	starting_time_pressure=starting_time_pressure+time_interval_pressure
	x_data_pressure=np.append(x_data_pressure,[starting_time_pressure])
	y_data_pressure=np.append(y_data_pressure,[y_val_pressure])
	line_pressure.set_xdata(x_data_pressure)
	line_pressure.set_ydata(y_data_pressure)
	# print(x_data)
	if y_val_pressure==5:
		y_val_pressure=-5
		return line_pressure,
	if y_val_pressure==-5:
		y_val_pressure=5
		return line_pressure,

fig_pressure=Figure(figsize=(7,2.3), dpi=100)
ax_pressure = fig_pressure.add_subplot(111)
ax_pressure.set_facecolor('xkcd:black')   #background color
fig_pressure.patch.set_facecolor('xkcd:black')
ax_pressure.set_xlim(0, 5)
ax_pressure.set_ylim(-12, 12)
line_pressure, = ax_pressure.plot(0, 0, color='white')
graph_pressure = FigureCanvasTkAgg(fig_pressure, master=window)
canvas_pressure=graph_pressure.get_tk_widget()
canvas_pressure.place(x=0,y=0)
animation_pressure = FuncAnimation(fig_pressure, func=animation_frame_pressure, frames=1000, interval=10)

window.mainloop()

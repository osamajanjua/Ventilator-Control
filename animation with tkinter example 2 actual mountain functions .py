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
total_time_pressure=5
data_points_pressure=total_time_pressure/time_interval_pressure
animation_loop_counter_pressure=0
def animation_frame_pressure(i):
	global time_interval_pressure
	global starting_time_pressure
	global y_val_pressure
	global x_data_pressure
	global y_data_pressure
	global animation_loop_counter_pressure
	starting_time_pressure=starting_time_pressure+time_interval_pressure
	if animation_loop_counter_pressure<data_points_pressure:
		x_data_pressure=np.append(x_data_pressure,[starting_time_pressure])
		y_data_pressure=np.append(y_data_pressure,[y_val_pressure])
	if animation_loop_counter_pressure>=data_points_pressure:
		y_data_pressure=np.append(y_data_pressure,[y_val_pressure])
		y_data_pressure=np.delete(y_data_pressure,0)
	line_pressure.set_xdata(x_data_pressure)
	line_pressure.set_ydata(y_data_pressure)
	animation_loop_counter_pressure=animation_loop_counter_pressure+1
	if y_val_pressure==5:
		y_val_pressure=-5
		return line_pressure,
	if y_val_pressure==-5:
		y_val_pressure=5
		return line_pressure,
total_time_pressure=5
fig_pressure=Figure(figsize=(7,2.3), dpi=100)
ax_pressure = fig_pressure.add_subplot(111)
ax_pressure.set_facecolor('xkcd:black')   #background color
fig_pressure.patch.set_facecolor('xkcd:black')
ax_pressure.set_xlim(0, total_time_pressure)
ax_pressure.set_ylim(-12, 12)
line_pressure, = ax_pressure.plot(0, 0, color='white')
graph_pressure = FigureCanvasTkAgg(fig_pressure, master=window)
canvas_pressure=graph_pressure.get_tk_widget()
canvas_pressure.place(x=0,y=0)
animation_pressure = FuncAnimation(fig_pressure, func=animation_frame_pressure, frames=1000, interval=10)

x_data_flow = np.array([0])
y_data_flow = np.array([0])
y_val_flow=5
starting_time_flow=0
time_interval_flow=0.1
total_time_flow=5
data_points_flow=total_time_flow/time_interval_flow
animation_loop_counter_flow=0
def animation_frame_flow(i):
	global starting_time_flow
	global y_val_flow
	global x_data_flow
	global y_data_flow
	global animation_loop_counter_flow
	starting_time_flow=starting_time_flow+time_interval_flow
	if animation_loop_counter_flow<data_points_flow:
		x_data_flow=np.append(x_data_flow,[starting_time_flow])
		y_data_flow=np.append(y_data_flow,[y_val_flow])
	if animation_loop_counter_flow>=data_points_flow:
		y_data_flow=np.append(y_data_flow,[y_val_flow])
		y_data_flow=np.delete(y_data_flow,0)
	line_flow.set_xdata(x_data_flow)
	line_flow.set_ydata(y_data_flow)
	animation_loop_counter_flow=animation_loop_counter_flow+1
	if y_val_flow==5:
		y_val_flow=-5
		return line_flow,
	if y_val_flow==-5:
		y_val_flow=5
		return line_flow,
	return line_flow,
fig_flow=Figure(figsize=(7,2.3), dpi=100)
ax_flow = fig_flow.add_subplot(111)
ax_flow.set_facecolor('xkcd:black')   #background color
fig_flow.patch.set_facecolor('xkcd:black')
ax_flow.set_xlim(0, total_time_flow)
ax_flow.set_ylim(-12, 12)
line_flow, = ax_flow.plot(0, 0, color='white')
graph_flow = FigureCanvasTkAgg(fig_flow, master=window)
canvas_flow=graph_flow.get_tk_widget()
animation2 = FuncAnimation(fig_flow, func=animation_frame_flow, frames=1000, interval=10)
def place_canvas():
	print("canvas is here")
	canvas_flow.place(x=0,y=500)
def hide_canvas():
	canvas_flow.place_forget()
quit_button_image=PhotoImage(file="tick.gif")
quit_button=Button(window, image=quit_button_image, highlightthickness=0,bd=0,bg="white",command=place_canvas)
quit_button.place(x=799,y=50)

quit2_button_image=PhotoImage(file="cross.gif")
quit2_button=Button(window, image=quit2_button_image, highlightthickness=0,bd=0,bg="white",command=hide_canvas)
quit2_button.place(x=799,y=120)

window.mainloop()

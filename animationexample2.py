from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = np.array([0])
y_data = np.array([0])
fig, ax = plt.subplots()
ax.set_xlim(0, 5)
ax.set_ylim(-12, 12)
line, = ax.plot(0, 0)

y_val=5
starting_time=0
time_interval=0.1
def animation_frame(i):
	global time_interval
	global starting_time
	global y_val
	global x_data
	global y_data
	starting_time=starting_time+time_interval
	x_data=np.append(x_data,[starting_time])
	y_data=np.append(y_data,[y_val])
	line.set_xdata(x_data)
	line.set_ydata(y_data)
	print(x_data)
	if y_val==5:
		y_val=0
		return line,
	if y_val==0:
		y_val=5
		return line,

animation = FuncAnimation(fig, func=animation_frame, frames=1000, interval=10)
plt.show()

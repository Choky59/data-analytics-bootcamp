# Dependencies
import matplotlib.pyplot as plt
import numpy as np

# Set x axis and variables
x_axis = np.arange(0, 10, 0.1)
sin = np.sin(x_axis)
cos = np.cos(x_axis)

# Draw a horizontal line with 0.25 transparency
plt.hlines(0, 0, 10, alpha=0.25)

# Each point on the sine chart is marked by a blue circle
sine_handle, = plt.plot(x_axis, sin, marker ='o', color='blue', label="Sine")
# Each point on the cosine chart is marked by a red triangle
cosine_handle, = plt.plot(x_axis, cos, marker='^', color='red', label="Cosine")

plt.legend(loc="lower right")

plt.savefig("./lineConfig.png")
plt.show()
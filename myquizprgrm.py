import matplotlib.pyplot as plt
import numpy as np

# Define bird-like shape using scatter points
x = np.array([0, 1, 2, 1.5, 1, 0, -1, -1.5, -2, -1])
y = np.array([0, 1, 0.5, -0.5, -1, -0.5, -1, -0.5, 0.5, 1])

plt.plot(x, y, 'bo-', linewidth=2)  # Connect points with a line
plt.title("Simple Bird Shape")
plt.axis("equal")
plt.show()

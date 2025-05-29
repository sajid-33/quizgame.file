import matplotlib.pyplot as plt

# Define square coordinates
x = [0, 1, 1, 0, 0]
y = [0, 0, 1, 1, 0]

# Plot the square
plt.plot(x, y, 'b-', linewidth=2)  # Blue lines
plt.fill(x, y, 'skyblue', alpha=0.5)  # Light blue fill
plt.title("Visualizing a Square")
plt.axis("equal")  # Keep proportions correct
plt.show()

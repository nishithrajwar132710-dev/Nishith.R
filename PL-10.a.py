import matplotlib.pyplot as plt

# Data
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Plot line
plt.plot(x, y)

# Labels and title
plt.xlabel('X Axis - Values')
plt.ylabel('Y Axis - Squares')
plt.title('Line Plot of Squares')

# Show plot
plt.show()

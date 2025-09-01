import matplotlib.pyplot as plt

# Data
x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]       # Squares
y2 = [0, 1, 8, 27, 64, 125]     # Cubes

# Plot both lines with custom colors
plt.plot(x, y1, color='blue', label='Squares')    # Red line
plt.plot(x, y2, color='black', label='Cubes')    # Green line

# Labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Squares and Cubes with Custom Colors')

# Show legend
plt.legend()

# Show plot
plt.show()


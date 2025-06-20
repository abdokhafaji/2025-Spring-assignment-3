import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file
data = np.loadtxt("01_trajectory.csv", delimiter=",")

# Extract columns
x_head = data[:, 0]
y_head = data[:, 1]
x_tail = data[:, 2]
y_tail = data[:, 3]

# Compute theta (orientation)
theta = np.arctan2(y_head - y_tail, x_head - x_tail)

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Subplot 1: Head and Tail Positions
axs[0].plot(x_head, y_head, 'r-', label='Head')
axs[0].plot(x_tail, y_tail, 'b-', label='Tail')
axs[0].set_title("Trajectory of the Robot")
axs[0].set_xlabel("x-axis")
axs[0].set_ylabel("y-axis")
axs[0].legend()

# Subplot 2: Orientation over Frames
axs[1].plot(range(len(theta)), theta, 'g-')
axs[1].set_title("Orientation of the Robot")
axs[1].set_xlabel("Frame")
axs[1].set_ylabel("Theta (rad)")

plt.tight_layout()
plt.show()

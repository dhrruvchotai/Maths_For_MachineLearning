import numpy as np
import matplotlib.pyplot as plt

# Generate time points
t = np.linspace(0, 40, 1000)  # start, finish, n points

# Calculate distances for the robber and sheriff
distRobber = 2.5 * t
distSheriff = 3 * (t - 5)

# Create the plot
fig, ax = plt.subplots()
plt.title('A Bank Robber Caught')
plt.xlabel('time (in minutes)')
plt.ylabel('distance (in km)')
ax.set_xlim([0, 40])
ax.set_ylim([0, 100])

# Plot the distances
ax.plot(t, distRobber, c='green', label='Robber')
ax.plot(t, distSheriff, c='brown', label='Sheriff')

# Add vertical and horizontal dashed lines
plt.axvline(x=30, color='purple', linestyle='--')
plt.axhline(y=75, color='purple', linestyle='--')

# Show the plot
plt.show()

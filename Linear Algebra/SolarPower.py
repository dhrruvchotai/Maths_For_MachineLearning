import numpy as np
import matplotlib.pyplot as plt

days = np.arange(0,60)

mark1 = days
mark2 = np.where(days>=30,(4*(days-30)),0) #here second param is for if condition is true and 3rd if condition is false.

plt.plot(days,mark1,label="mark1 1kJ/day",color="blue",marker=".",markersize=2,markeredgecolor="black")
plt.plot(days,mark2,label="mark2 4kJ/day",color="red",marker=".",markersize=2,markeredgecolor="black")

plt.axvline(x=40, color="green", linestyle="--", label="Equal Energy (May 11)")
plt.axhline(y=40, color="green", linestyle="--")

plt.xlabel("Days since April 1st")
plt.ylabel("Total Energy Generated (kJ)")
plt.legend()

plt.show()
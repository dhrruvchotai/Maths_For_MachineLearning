import numpy as np
import matplotlib.pyplot as plt

#Y = 3X
#-5X+2Y = 2

x = np.linspace(-100,100,1000)
y1 = 3*x
y2 = (2+5*x)/2

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.xlim([0,3])
plt.ylim([0,10])

plt.plot(x,y1,label="y=3x",color="brown",marker=".",markersize=10,markeredgecolor="black")
plt.plot(x,y2,label="(2+5*x)/2",color="green",marker=".",markersize=10,markeredgecolor="black")

plt.axhline(y=6,color="red",linestyle="--")
plt.axvline(x=2,color="blue",linestyle="--")

plt.plot(2,6,'ro', markersize=10, label="Intersection") #ro = red marker and o = circular marker

plt.legend()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

v = np.array([3, 1])

def plot_vectors(vectors, colors):
    plt.figure()
    plt.axvline(x=0, color='lightgray')
    plt.axhline(y=0, color='lightgray')

    for i in range(len(vectors)):
        x = np.concatenate([[0,0],vectors[i]])
        plt.quiver([x[0]], [x[1]], [x[2]], [x[3]],color=colors[i])

plot_vectors([v], ['lightblue'])
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.show()
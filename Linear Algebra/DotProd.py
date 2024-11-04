import numpy as np
import torch
import tensorflow as tf

#in numpy
X = np.array([1,2,3.])
Y  = np.array([4,5,6.])

dotp = 1*4 + 2*5 + 3*6
ans = np.dot(X,Y)

print(f"without func : {dotp}")
print(f"with func : {ans}")

#pytorch
A = torch.tensor([1,2,3.])
B  = torch.tensor([4,5,6.])

dotp = 1*4 + 2*5 + 3*6
ans1 = torch.dot(A,B)

print(f"without func : {dotp}")
print(f"with func : {ans1}")


#tensorflow
C = tf.Variable([1,2,3.])
D  = tf.Variable([4,5,6.])

dotp = 1*4 + 2*5 + 3*6
ans2 = tf.reduce_sum(tf.multiply(C,D))

print(f"without func : {dotp}")
print(f"with func : {ans2}")
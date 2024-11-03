import numpy as np
import tensorflow as tf
import torch

X = np.array([[25,2],[5,26],[3,7]])

#Numpy
print(X*2)
print(X+2)
print(X*2+2)


#Pytorch

#Python operators are overloaded alternatively use torch.mul() or torch.add4
Y = torch.tensor([[25,2],[5,26],[3,7]])
print(torch.add(torch.mul(Y,2),2))

#Using Tensorflow

#tf.multiply() or tf.add()
Z = tf.Variable([[25,2],[5,26],[3,7]])
print(tf.add(tf.multiply(Z,2),2))



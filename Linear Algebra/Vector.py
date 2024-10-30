import numpy as np
import torch
import tensorflow as tf

#IN NUMPY

x = np.array([11,2,34])
# in 1-D array transpose has no effect in shape and all.
#however if you want to check the shape in 1-D the you can write it like this
x = np.array([[11,1212,134]])

print(f"shape of x is : {x.shape}")
print(f"shape of transpose of x is : {(x.T).shape}")

x = np.array([[1,2,3],[4,5,6]])

tranposeX = x.T #here T is for transpose.

print(f"normal x is : {x}")
print(f"transpose of x is : {tranposeX}")

print(f'shape of x {x.shape}')
print(f'shape of transpose of x {tranposeX.shape}')


#IN PYTORCH

print("\n")

x = torch.tensor([121,2,332])
print(f"vector using pytorch : {x}")

#IN TENSORFLOW
x = tf.Variable([212,33,21])
print(f"vector using tensorflow : {x}")

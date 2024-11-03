import numpy as np
import torch
import tensorflow as tf

A = np.array([[25,2],[5,26],[3,7]])
print(f"Matrix : {A}")
print(f"Matrix shape : {A.shape}")
print(f"Matrix size : {A.size}")

#Select left column of the matrix A
leftcol = A[:,0]
print(f"Left column is {leftcol}")

#Select middle row of the matrix A
midrow = A[1,:]
print(f"Mid row is : {midrow}")


#In PyTorch
B = torch.tensor([[25,2],[5,26],[3,7]])
print(f"Matrix : {B}")
print(f"Matrix shape : {B.shape}")

#Select middle row of the matrix B
midrow = B[1,:]

print(f"Mid row is : {midrow}")

#In TensorFlow
C = tf.Variable([[25,2],[5,26],[3,7]])

print(f"Matrix : {C}")
print(f"Matrix : {tf.rank(C)}") #rank means how dimension tensor it is so matrix is 2d tensor
print(f"Matrix shape : {tf.shape(C)}")

#Select middle row of the matrix C
midrow = C[1,:]
print(f"Mid row is : {midrow}")


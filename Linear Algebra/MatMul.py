import numpy as np
import torch
import tensorflow as tf

# #mat-vec multiplication
# X = np.array([[3,4],[5,6],[7,8]])
# a = np.array([1,2]) #we can say it is a vector because it has only one row

# ans = np.dot(X,a)
# print(f"multiplication is : {ans}")

# #in pytorch it is matmul() method
# #in tensorflow it is tf.linalg.matvec() -> matvec means ke matrix by vector multiplication

# #mat-mat multiplication
# Y = np.array([[3,4],[5,6],[7,8]])
# Z = np.array([1,9],[2,0]) 

# print(f"the ans of multiply is {np.dot(Y,Z)} ")


# #in pytorch
# X = torch.tensor([[3,4],[5,6],[7,8]])
# A = torch.tensor([[1,9],[2,0]])

# print(f"the ans is {torch.matmul(X,A)}")

#in tensorflow
C = tf.Variable([[3,4],[5,6],[7,8]])
D = tf.Variable([[1,9],[2,0]])

print(f"the ans is : {tf.matmul(C,D)}")
#in tensorflow for mat-mat multiplication it is matmul function 

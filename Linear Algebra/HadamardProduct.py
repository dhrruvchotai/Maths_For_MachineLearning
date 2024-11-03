import numpy as np

X = np.array([[1,2],[3,4],[5,6]])
A = X+2

print(X)
print(A)

print(A*X) #This is Hadamard product
#Multiply corresponding elements with each other this is not a matrix multiplication

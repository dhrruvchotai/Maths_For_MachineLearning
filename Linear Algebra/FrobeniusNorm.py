import numpy as np

#it measures the distance from the origin as L2 Norm determines


X = np.array([[1,2],[3,4]])

#manually
ans = (1**2 + 2**2 + 3**2 + 4**2)**(1/2)

print(f"the frobenius norm is : {ans}")

#inbuilt numpy method
ans1 = np.linalg.norm(X)

print(f"The frobenius norm is : {ans1}")


#Similarly 
#in pytorch it is torch.norm() method and
#in tensorflow it is tf.norm() method


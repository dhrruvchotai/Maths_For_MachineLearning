import numpy as np


vector = [25,2,5]

# L2 Norm: 

#manually
ans = (25**2 + 2**2 + 5**2)**(1/2)
print(f"L2 Norm of the vector is : {ans}")

#using numpy method
ans1 = np.linalg.norm(vector) #it gives length(magnitude) of the vector.
print(f"Using numpy method l2norm is : {ans1}")

#Squared L2 Norm : 

#manually
ans2 = (25**2 + 2**2 + 5**2)
print(f"Squared L2 Norm of the vector is : {ans2}")

ans3 =  np.dot(vector,vector)
print(f"Using numpy method Squared l2norm is : {ans3}")




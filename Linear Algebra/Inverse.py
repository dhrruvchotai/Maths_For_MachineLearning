import numpy as np
X = np.array([[4,2],[-5,-3]])

Xinv  = np.linalg.inv(X)

print(f"xinv is : {Xinv}")

y = np.array([4,-7])

ans = np.dot(Xinv,y)

print(f"the ans is {ans}")
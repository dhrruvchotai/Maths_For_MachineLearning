import numpy as np

X = np.array([[25,2],[5,26],[3,7]])

print(X.sum())

#same in pytorch sum() method
#and in tensorflow it is reduce_sum method

#for sum of rows use
print(X.sum(axis = 0)) #ans = [[25+5+3],[2+26+7]]
#and for cols
print(X.sum(axis=1)) #ans = [[25+2],[5+26],[3+7]]

#in pytorch it is sum(arr,0) or sum(arr,1)
#in tensorflow it is reduce_sum(arr,0) or reduce_sum(arr,1)





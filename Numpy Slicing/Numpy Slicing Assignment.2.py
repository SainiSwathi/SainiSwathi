#2.Write a Numpy program to create a 3x3 matrix with values ranging from 2 to 10.


import numpy as np

#Create a 3x3 matrix with values ranging from 2 to 10
Matrix=np.arange(2,11).reshape(3,3)

print("3x3 Matrix:")
print(Matrix)

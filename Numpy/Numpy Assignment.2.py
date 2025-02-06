#2.Covert the below list into a numpy array then display the array then display the first and last index and the  multiply each element by 2 and display the result.
#Input:my_list=[1,2,3,4,5]

import numpy as np
my_list=[1,2,3,4,5]
my_array=np.array(my_list)

print("original array:")
print(my_array)

print("First Element:", my_array[0])
print("Last Elemnt:", my_array[-1])

my_array*=2

print("Array after multiplying each element by 2:")
print(my_array)

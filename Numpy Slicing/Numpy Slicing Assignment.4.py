#4.Write a Numpy program to convert a list and tuple into arrays.
#Input:my_lis=[1,2,3,4,5,6,7,8]
#Input:my_tuple=([8,4,6],[1,2,3])

import numpy as np
#Input list
my_list=[1,2,3,4,5,6,7,8]

#Input tuple
my_tuple=([8,4,6],[1,2,3])

#Convert list to array
list_array=np.array(my_list)

#convert tuple to array
tuple_array=np.array(my_tuple)

print("List converted to array:")
print(list_array)

print("tuple converted to array:")
print(tuple_array)

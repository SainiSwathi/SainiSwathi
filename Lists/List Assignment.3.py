#3. Write a Python program to find duplicate values from a list and display those. 

my_list = [1,2,2,3,4,5,5,5,6,7]
duplicate_l = list(set([i for i in my_list if my_list.count(i)>1]))
print(f"List : {my_list}")
print(f"Duplicate elements of the list: {duplicate_l}") 


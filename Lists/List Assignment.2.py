#2. Write a Python program to get the largest and smallest number from a list without builtin functions builtin functions. 

my_list= [12, 45, 7, 23, 56, 89, 34]
min_num = my_list[0]
max_num = my_list[0]
for num in my_list:
    if num < min_num:
        min_num = num
    elif num > max_num:
        max_num
print(f'min num from the list = {min_num}\\nmax num from the list = {max_num}')

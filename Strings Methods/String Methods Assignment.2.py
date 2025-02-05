#2. Write a Python program to remove duplicate characters of a given string. 


input_str = 'String and String Function'

new_str = ''

for word in input_str.split():
    if word not in new_str:
        new_str += word + ' '

new_str

#2. Write a Python program to remove a newline in Python 

string = "\nBest \nDeeptech \nPython \nTraining\n"
new_str = ''
for char in string:
    if char not in'\\n':
        new_str += char
        new_str

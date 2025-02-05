#1. Write a Python program to Count all letters, digits, and special symbols from the given string 

#Input = “P@#yn26at^&i5ve” 

#Output: Chars = 8 Digits = 2 Symbol = 3


input_str = "P@#yn26at^&i5ve"
# Output: Chars = 8 Digits = 3 Symbol = 4
# to check alphabets --> isalpha()
# to check digits --> isdigits()
# special symbols --> else

alpha = 0
digits = 0
symbols = 0

for char in input_str:
    if char.isalpha():
        alpha += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1

print(f'Chars = {alpha} Digits = {digits} Symbol = {symbols}')

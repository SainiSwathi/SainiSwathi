#3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” 

#Output: 

#UpperCase : 5 

#LowerCase : 18 

#NumberCase : 5 

#SpecialCase : 11

input_str = 'Hell0 W0rld ! 123 * # welcome to pYtHoN' 

upper_cnt = 0
lower_cnt = 0
digit_cnt = 0
symbol_cnt = 0

for char in input_str:
    if char.isupper():
        upper_cnt += 1
    elif char.islower():
        lower_cnt += 1
    elif char.isdigit():
        digit_cnt += 1
    else:
        symbol_cnt += 1

print(f'upper_cnt = {upper_cnt}\nlower_cnt = {lower_cnt}\ndigit_cnt = {digit_cnt}\nsymbol_cnt = {symbol_cnt}')

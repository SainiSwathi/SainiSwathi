#4. Write a Python Count vowels in a string 

input_str= 'Welcome to Python Assignment'

#Output: Total vowels are: 8

vowels = 'aeiou'
vowel_cnt = {}
for char in input_str:
    if char.lower() in vowel_cnt:
        vowel_cnt[char.lower()] += 1
    elif char.lower() in vowels:
            vowel_cnt[char.lower()] = 1
print(vowel_cnt)

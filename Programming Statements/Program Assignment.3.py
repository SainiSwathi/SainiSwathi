#3.Write a Program to Convert Kilometers to Miles.
kilometers = float(input('Enter the distance in km: '))

#1 kilometer = 0.621371 miles

conversion_factor = 0.621371

miles = kilometers * conversion_factor
print(f'{kilometers} km in miles is = {miles:.2f}')


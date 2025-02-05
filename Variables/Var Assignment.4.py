#4. Python program to find the area of a triangle whose sides are given.
base = float(input("Enter the base length of triangle: "))
height = float(input("Enter the height of the triangle: "))

area = (1/2) * base * height

print(f'Area of triangle with base {base} and height {height} = {area:2f}')

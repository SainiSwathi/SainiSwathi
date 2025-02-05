#2.Using input function take two number and then swap the number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Before swapping:")
print("Num 1:", num1)
print("Num 2:", num2)

num1, num2 = num2, num1

print("After swapping:")
print("Num 1:", num1)
print("Num 2:", num2)

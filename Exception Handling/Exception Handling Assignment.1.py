#1. Write a python program to handle a ZeroDivisionError Exception when dividing a number by Zero.


def divide_numbers(num1, num2):
    try:
        result=num1/num2
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

#Testing the fun
divide_numbers(10,2)
divide_numbers(10,0)



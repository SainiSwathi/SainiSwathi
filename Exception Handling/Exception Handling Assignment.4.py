#4. Write a python program that prompts the user to two numbers and raises a TypeError exception if the inputs are not numerical.

def get_numerical_input():
    while True:
        try:
            num1=float(input("please enter the first number: "))
            num2=float(input("please enter the second number: "))
            print("you entered:", num1, "and", num2)
            break
        except ValueError:
                    print("Error: Invalid input. please enter numerical values only.")

get_numerical_input()
            

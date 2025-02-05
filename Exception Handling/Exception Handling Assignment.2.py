#2. Write a python program that prompts the user to input an interger and raises a ValueError exception if the input is not a vaild integer.

def get_integer_input():
    while True:
        try:
            user_input = int(input("Please enter an integer: "))
            print("You entered:", user_input)
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

            get_integer_input()

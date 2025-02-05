#4. Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers

sum_of_numbers = 0

while True:
  number = int(input("Enter a number (enter 0 to stop): "))
  if number == 0:
    break
  sum_of_numbers += number

print("Sum of all entered numbers:", sum_of_numbers)

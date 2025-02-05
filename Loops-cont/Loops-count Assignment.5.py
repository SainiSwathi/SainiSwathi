#5. Python program to check the validity of password input by users.

password=input("Enter a password: ")

if len(password)<8:
    print("password is too short.")
elif not any(char.isdigit() for char in password):
    print("password must contain at least"
          "one digit.")
elif not any(char.isupper() for char in password):
    print("password must contain at least"
          "one uppercase letter.")

elif not any(char.islower() for char in password):
    print("password must contain at least"
          "one lowercase letter.")
else:
    print("password is vaild.")

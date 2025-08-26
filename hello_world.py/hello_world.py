# hello_world.py
# A simple program to greet a user and check their password.

def greet_user():
    name = input("What is your name? ")
    print(f"Hello, {name}!")

def check_password():
    password = input("Enter a password to check: ")
    if len(password) >= 8:
        print("That password is strong enough.")
    else:
        print("Password is too weak. Use at least 8 characters.")

# Run the program
greet_user()
check_password()
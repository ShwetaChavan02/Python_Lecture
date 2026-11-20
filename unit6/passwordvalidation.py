#password validation program
# the password should only contain alphabets, no numbers or special characters
# ascii values
# a 65 z 90
# A 97 Z 122

try:
    password=input("Enter your password:")
    if len(password)<8:
        raise ValueError("Password must be at least 8 characters long")
    if not password.isalpha():
        raise ValueError("Password should only contain alphabets")
    print("Password is valid")
except ValueError as e:
    print("Error:", e)
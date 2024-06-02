# String Length Checker
# Write a function that checks the length of a string provided by the user. 
# Handle the TypeError by raising a custom exception if the input is not a string.

a = input("Enter string and i will return lenght of string: ")

def length_checker(string):
    if string.isdigit():
        raise ValueError("This is a number.")
    return len(string)

try:
    print(length_checker(a))
except ValueError as e:
    print(e)
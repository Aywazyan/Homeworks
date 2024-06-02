# Write a Python program to check whether a given string is number or
# not using Lambda.

num_or_not = lambda x: True if int(x) else False

num_str = input("Enter String: ")

print(num_or_not(num_str))
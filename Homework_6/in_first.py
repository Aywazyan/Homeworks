# Write a Python function that takes two sets as input and returns a new set containing
# elements that are present in the first set but not in the second set.

a = set(input("Enter set number 1: "))
b = set(input("Enter set number 2: "))
c = a - b

print(c)
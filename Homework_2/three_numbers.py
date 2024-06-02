# Input three integers. 
# Output the word “Sorted” if the numbers are listed in a non-increasing or non-decreasing order and “Unsorted” otherwise.
# Sample Input
# 123
# 132
# 5 0 -4
# 999
# 990
# Sample Output
# Sorted
# Unsorted
# Sorted
# Sorted
# Sorted

a = input("Enter first 1 digit number: ")
b = input("Enter second 1 digit number: ")
c = input("Enter third 1 digit number: ")

if a < b and b < c:
    print("Sorted")
else:
    print("Unsorted")
# Write a Python function that takes two sets as input and returns a new set containing
# elements that are present in either of the input sets, but not in both

a = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
b = {'apple', 'orange', 'apple', 'pear', 'orange', 'watermelon'}
c = a ^ b 

print(c)
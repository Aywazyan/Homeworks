# Exercise 3: Average Function
# Write a function that calculates the average of a list of numbers

def calculate_average(lst):
    return sum(lst) / len(lst)

ex_list = [1,2,3,4,5]

print(calculate_average(ex_list))
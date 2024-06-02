# Exercise 5: Sum of Squares Function
# Write a function that calculates the sum of squares of numbers from 1 to n.

def sum_of_squares(n):
    total = 0
    num = 1
    while num <= n:
        total += num ** 2
        num += 1
    return total

print(sum_of_squares(4))
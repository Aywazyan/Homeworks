# Given the salaries of three employees working at a department, 
# find the amount of money by which the salary of the highest-paid employee differs from the salary of the lowest-paid employee. 
# The input consists of three positive integers - the salaries of the employees. 
# Output a single number, the difference between the top and the bottom salaries

# Sample Input      # Sample Output
# 100 500 1000      # 900
# 500 100 1000      # 900
# 36 11 20          # 25
# 20 20 20          # 0


sal_1 = input("First salary: ")
sal_2 = input("Second salary: ")
sal_3 = input("Third salary: ")

a = int(sal_1)
b = int(sal_2)
c = int(sal_3)
d = [a, b, c]

# if a > b > c:
#     print(a - c)

# if a < b < c:
#     print(c - a)

# if a > b < c:
#     print(a - b)

# if a < b > c:
#     if a > c:
#         print(b - c)
#     else:
#         print(b - a)

# if a == b == c:
#     print(0)

print(max(d) - min(d))
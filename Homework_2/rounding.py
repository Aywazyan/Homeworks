# Given a real number, round it to the nearest whole.

# Sample Input        Sample Output
# 0.3                 0
# 1.2398              1
# 1.5                 2
# 67.567              68

num = input("Please enter number: ")

float_num = float(num)

res = int(float_num-0.5)+1


print(res)
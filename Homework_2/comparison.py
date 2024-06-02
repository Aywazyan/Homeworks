# Input two positive integers, and output a line describing their relation. 
# Follow the sample format.
# Sample Input
# 79
# 11 11
# 4 - 4
# Sample Output
# 7 < 9
# 11 = 11
# 4 > -4

num = input("Enter two digit number: ")

def check(num):
    if num[0] > num[1]:
        print(f"{num[0]} > {num[1]}")
        
    elif num[0] < num[1]:
        print(f"{num[0]} < {num[1]}")
        
    else:
        print(f"{num[0]} = {num[1]}")

check(num)
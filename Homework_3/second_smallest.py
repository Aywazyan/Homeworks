# 4 Write a Python program to find the second smallest number in a list.

a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")
d = input("Enter fourth number: ")

list_1 = [a,b,c,d]
# smallest = list_1[0]

# for x in list_1:
#     if x < smallest: 
#         smallest = x

# second_smallest = smallest
# for x in list_1:
#     if x != smallest and (second_smallest is smallest or x < second_smallest):
#         second_smallest = x
# print(second_smallest)

print(sorted([a, b, c, d])[1])

def is_valid_input(x):
    if x.isnumeric():
        return True
    return False

list1 = [int(num) if is_valid_input(num) else ord(num) for num in list_1]

print(list1)

print(sorted(list1)[1])
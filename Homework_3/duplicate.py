# 5 Write a Python program to remove duplicates from a list.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

list_1 = [a,b,c,d]
list_2 = list_1[0]
duplicate = []

for x in list_1:
    if x == list_1[0]: 
        list_1[0] = x
        duplicate.append(x)
print(duplicate)

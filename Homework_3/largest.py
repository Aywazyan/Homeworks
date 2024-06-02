# 2 Write a Python program to get the largest number from a list.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

list_1 = [a,b,c,d]
largest = list_1[0]

for x in list_1:
    if x > largest: 
        largest = x
print(largest)
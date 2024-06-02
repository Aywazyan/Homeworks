# 3 Write a Python program to get the smallest number from a list.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

list_1 = [a,b,c,d]
smallest = list_1[0]

for x in list_1:
    if x < smallest: 
        smallest = x
print(smallest)
# 6 Turn every item of a list into its square

lisst = [int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: ")), int(input("Enter fourth number: ")), int(input("Enter fifth number: "))]
square = []

for num in lisst:
    square.append(num ** 2)

print(square)

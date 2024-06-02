# Print the even numbers from 0 to 20 using a for loop and the range function
l = []

for x in range(21):
    if x % 2 == 0:
        l.append(x)
print(f"Even numbers are {l}")
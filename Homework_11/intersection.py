# Write a Python program to find intersection of two given arrays using
# Lambda.

# Original arrays:
x = [1, 2, 3, 5, 7, 8, 9, 10]
y =  [1, 2, 4, 8, 9]

intersect = lambda x, y: list(filter(lambda z: z in x, y))

print(intersect(x,y))
# Write a Python program to square and cube every number in a given list of
# integers using Lambda.
# Sample. ([1,2,3,4,5])
# Output: ([1, 4, 9, 16, 25], [1, 8, 27, 64, 125])


lst = [1,2,3,4,5]
square = lambda x : x ** 2
cube = lambda x : x ** 3

print(list(map(square, lst)))
print(list(map(cube, lst)))
# Write a Python program to find if a given string starts with a given
# character using Lambda.

starts_with = lambda x, y: x[0] == (y)

string = input("Enter your text: ")
start = input("Enter character to check: ")

res = starts_with(string, start)

print(res)
# 1. Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# Example:
# Sample String : 'w3resource'
# Expected Result : 'w3ce' 
# __________________________ 
# Sample String : 'w3'
# Expected Result : 'w3w3'


word = "Python"

result= word[:2] + word[-2:]

print(result)
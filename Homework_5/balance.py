# Write a program to check if two strings are balanced. For example, 
# strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
# The character’s position doesn’t matter.

s1 = "Yn"
s1 = s1.lower()
s2 = "PYnative"
s2 = s2.lower()

char = True

for i in s1:
    if i not in s2:
        char = False

if char == True:
    print(True)
else:
    print(False)

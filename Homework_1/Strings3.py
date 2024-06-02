# Write a Python program to remove the n-th index character from a nonempty string.
# Example:
# Sample string: ‘abcdefgh’
# n-3
# Expected result: abcefgh

word = "Python"

n = 2

new_word = word[:n]

new_word2 = word[-n:]

result = new_word + new_word2

print(result)
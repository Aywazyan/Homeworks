# Create a string made of the first, middle and last character of given string with odd number of symbols
# Example:
# Sample = ‘Sevak’
# Expected ‘Svk’

word = "Spartak"

lenght = len(word)

middle = int(lenght / 2)

middle_word = word[middle]

result = word[0] + middle_word +word[-1]

print(result)
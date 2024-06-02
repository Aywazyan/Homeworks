# 9. Append new string in the middle of a given (even number of characters) string Example:
# Sample = ‘python’ new_string = ‘new’ Expected ‘pytnewhon

word_1 = "Ayvazyan"
word_2 = "Erik"

lenght = len(word_1)

middle = int(lenght / 2)

result = word_1[:middle] + word_2 + word_1[middle:]


print(result)
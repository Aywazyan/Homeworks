# Implement a Python program that reads a text file (input.txt), prompts the user
# for a word to find, and another word to replace it with. Replace all occurrences of
# the first word with the second word and save the modified text to a new file
# (output.txt).

input_file = "input.txt"
output_file = "output.txt"

word_to_find = input("Enter the word to find: ")
replacement_word = input("Enter the word to replace it with: ")

with open(input_file, 'r') as file:
    text = file.read()

modified_text = text.replace(word_to_find, replacement_word)

with open(output_file, 'w') as file:
    file.write(modified_text)

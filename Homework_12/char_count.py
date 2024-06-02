# Character count :
# Write a Python script that reads a text file (input.txt) and counts the
# occurrences of each character (including spaces and punctuation). Output the
# character frequency to another text file (output.txt).

def char_count(file):
    with open('input.txt') as file:
        text = file.read()
    
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    with open('output.txt', 'w', encoding='utf-8') as file:
        for char, count in sorted(char_count.items()):
            file.write(f"'{char}': {count}\n")
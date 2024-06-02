# Random Password Generator:
# Write a function that generates a random password for the user. 
# Allow the user to specify the length and complexity of the password (include letters, numbers, and symbols).
# Ogtvel random u string module-neric (string.ascii_letters, string.digits,string.punctuation, )

import random
import string

def generate_password(length):
    characters = ''
    letters = False if input("If you don't want to use letters in your password, type \"no\": ").lower() == 'no' else True
    digits = False if input("If you don't want to use digits in your password, type \"no\": ").lower() == 'no' else True
    symbols = False if input("If you don't want to use symbols in your password, type \"no\": ").lower() == 'no' else True
    if sum([letters, digits, symbols]) == 0:
        return "You have to choose at lease one"
    for _ in range(length):
            if letters:
                characters += random.choice(string.ascii_letters)
            if digits:
                characters += random.choice(string.digits)
            if symbols:
                characters += random.choice(string.punctuation)
    return characters


if __name__ == '__main__':
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)

    if password:
        print("Generated Password:", password)
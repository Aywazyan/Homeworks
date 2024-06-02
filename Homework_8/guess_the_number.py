import random

random_number = random.randint(1, 100)


user_number = 0

while user_number != random_number:
    user_number = int(input("Guess the number from 1 to 100: "))
    if user_number < random_number:
        print("Your number is smaller")
    elif user_number > random_number:
        print("Your number is greater")
    else:
        print("Congratulations")
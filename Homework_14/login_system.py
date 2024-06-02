# Login System
# Write a simple login system where the user enters a username and password. 
# Handle the KeyError by raising a custom exception if the username is not found in the users database(dictionary).

def login(username, password, users):
    try:
        if users[username] == password:
            print("Login successful!")
        else:
            print("Incorrect password!")
    except KeyError:
        print("User not found")

users = {"spartak": "password123","vazgen": "666negzav","baghdasar": "bxdo2121"}

username = input("Enter username: ")
password = input("Enter password: ")

login(username, password, users)
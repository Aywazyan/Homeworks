# Type Conversion:
# Write a function that prompts the user to enter a number and tries to convert it to an integer. 
# Handle the TypeError exception by printing a message indicating that the input is not a valid number. 
# Use a finally block to print "Type conversion process completed."

def convert_to_integer():
    try:
        number = input("Enter a number: ")
        integer_number = int(number)
        print("Integer value:", integer_number)
    except ValueError:
        print("Input is not a valid number.")
    finally:
        print("Type conversion process completed.")

convert_to_integer()

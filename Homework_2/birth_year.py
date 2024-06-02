# The program prompts the user their birth year. 
# Assuming a person’s age is a non-negative integer not exceeding 120, output the user’s age or the words “Incorrect Year”. 
# The sample outputs assume it’s currently the year 2016. If you are writing this program during any other year, the correct answers may differ. 
# Store the value of the current year in a variable.
# Sample Input
# 2016
# 2018
# 1903
# 1803
# 1991
# Sample Output
# 0
# Incorrect Year
# 113
# Incorrect Year
# 25

m = 2024
n = 120
year = input("Enter your birth year: ")

if int(year) < m - 120:
    print("Incorrect Year")
elif int(year) > m:
    print("Incorrect Year")
else:
    print("Your age is: ", m - int(year))
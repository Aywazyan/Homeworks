# Count all letters, digits, and special symbols from a given string

txt = "P@#yn26at^&i5ve"

letters = 0
digits = 0
symbols = 0


for i in txt:
    if ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122:
        letters += 1
    elif ord(i) >= 48 and ord(i) <= 57:
        digits += 1
    else:
        symbols += 1

print(f"Total counts of letters is {letters}, digits {digits}, and symbols {symbols}")


for i in txt:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
    else:
        symbols += 1

print(f"Total counts of letters is {letters//2}, digits {digits//2}, and symbols {symbols//2}")
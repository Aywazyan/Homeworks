# Write a Python function to calculate count of each letter in string

def letters_counter(string):
    res = {}  
    for x in string:
        if x in res:
            res[x] += 1
        else:
            res[x] = 1
    return res

print(letters_counter("calculation"))
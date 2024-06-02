# List Element Removal
# Write a function that removes an element at a specified index from a list. 
# Handle the IndexError by raising a custom exception if the index is out of range.

def remove_element(lst, index):
    if index < 0 or index >= len(lst):
        raise IndexError("Index out of range")
    return lst.pop(index)

my_list = [1, 2, 3, 4, 5]

try:
    removed_element = remove_element(my_list, 2)
    print("Removed element:", removed_element)
    print("Updated list:", my_list)
except IndexError as e:
    print(e)

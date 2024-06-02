# You are given three lists, list1, list2, and list3. Your task is to implement a
# programm that takes these lists and prints the following:
# The set of elements that are common to all three lists.
# The set of elements that are present in at least two of the three lists, but not in all three.
# The set of elements that are unique to each list (present in only one list).

list_1 = ['apple', 'orange', 'apple', 'pear', 'banana']
list_2 = ['apple', 'orange', 'apple', 'pear', 'kiwi']
list_3 = ['apple', 'orange', 'kiwi', 'pear', 'peach']

sett_1 = set(list_1)
sett_2 = set(list_2)
sett_3 = set(list_3)


print("Exist in all 3 lists: ", sett_1 & sett_2 & sett_3)

a = sett_1 & sett_2
b = sett_1 & sett_3
c = sett_2 & sett_3

d = a | b | c
e = sett_1 & sett_2 & sett_3


print("Exist at least in 2 but not in 3", d - e)

print("Exist only in one list " , sett_1 - sett_2 - sett_3 )
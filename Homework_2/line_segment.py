# You are given four real numbers- a1, b1, a2, b2 - The endpoints of two line segments on a line. 
# Find the length of their intersection. 
# Note that the order of the endpoints of a segment is irrelevant, i.e. 
# the segments [1;2] and [2;1] are considered the same.

# Sample Input          Sample Output
# 1 4
# 9 7                   0
# 1 2.5                 
# 3 2                   0.5
# 10 0                  
# 0.1 0.2               0.1

a1 = float(input("Please enter 1 start point: "))
b1 = float(input("Please enter 1 end point: "))
a2 = float(input("Please enter 2 start point: "))
b2 = float(input("Please enter 2 end point: "))

my_list = [a1, b1]
my_list2 = [a2, b2]

c = sorted(my_list)
d = sorted(my_list2)
print(f"First line is {c}, and second is {d}")

if max(c[0], d[0]) <= min(c[1], d[1]):
    print(min(c[1], d[1]) - max(c[0], d[0]))  
else:
    print(0)

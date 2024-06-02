# You are given four real numbers - the coordinates of two points on a plane. 
# The first two numbers are the x and y coordinates of the first point, 
# and the last two numbers are the x and y coordinates of the second point. 
# Output the length of the line segment bounded by the two points.

# Sample Input            Sample Output
# 1 2.2 
# 2.5 -1.5                3.9924

# 0.0 0.0                  
#3.0 4.0                  5

x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))

z = x2 - x1
c = y2 - y1

res = (z **2) + (c **2)
print(res ** 0.5)
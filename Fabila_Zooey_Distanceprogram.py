import math

# Ask for the x coordinates
x1 = float(input("x1: "))
x2 = float(input("x2: "))
# Ask for the y coordinates
y1 = float(input("y1: "))
y2 = float(input("y2: "))

# Use the math import
# The formula is: d = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
x_sq = math.pow(x2 - x1, 2) 
y_sq = math.pow(y2 - y1, 2)
distance = math.sqrt(x_sq + y_sq)

# Display the results
print(f"the distance is: {distance:2f},)

# Using a library is more practical because it lets the user focus on making programs easier, rather than focusing on making a 
# complicated code for a simple task. It also reduces the time needed for making programs, especially as a student.
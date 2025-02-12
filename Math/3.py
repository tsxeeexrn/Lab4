import math
sides = int(input()) 
length = int(input()) 
polygon = (sides * length**2) / (4 * math.tan(math.pi / sides))
print(polygon)

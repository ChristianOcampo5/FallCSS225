import math

# Christian Ocampo
# 11/03/24
# Problem 5 - degrees.py
# Using the math degree function

radian_value = float(input("Enter the angle in radians:")) # User can type in number

degrees_manual = radian_value * (180 / math.pi) # Converts the number to a degree

degrees_math = math.degrees(radian_value) # Converts the numbers to degrees by using the math degrees function

print("Degrees (manual calculation):", degrees_manual)
print("Degrees (using math.degrees):", degrees_math)
# Both values are printed
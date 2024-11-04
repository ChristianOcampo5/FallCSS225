import math

# Christian Ocampo
# 11/03/24
# Problem 6 - factorial.py
# Using the factorial function while only inputting positive numbers

num = int(input("Enter a positive integer to calculate its factorial: ")) # users can enter a number

# Calculate factorial using a for loop function
factorial_manual = 1
for i in range(1, num + 1):
    factorial_manual *= 1

# Calculate number using the math factorial function
factorial_math = math.factorial(num)

# Both values are printed
print("Factorial (calculated manually):", factorial_manual)
print("Factorial (using math.factorial):", factorial_math)
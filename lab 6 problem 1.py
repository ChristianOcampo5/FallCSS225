import random

# Christian Ocampo
# 11/03/24
# Problem 1 - randomrange.py
# Using the for function to find the y while printing 10

# The for function to print numbers between 25 and 36
for _ in range(10):
    y = random.randrange(25, 36)
# 36 is exclusive, this will give a number between 25 and 35 inclusive
    print(y)
# colum of numbers are printed
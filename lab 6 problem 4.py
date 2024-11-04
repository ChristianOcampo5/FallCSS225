import math

num_terms = 100000 # number of terms to use in the approximation

approx_pi = 0 # Initialize the approximation of pi

# Christian Ocampo
# 11/03/24
# Problem 4 - pi.py
# Using the pi function to find the approximation

for i in range(num_terms):
# calculating the approximation using the leibniz formula
    term = (-1)**i / (2 * i + 1)
# compute each term in the series
    approx_pi += term

approx_pi *= 4 # multiplying by 4 to get the approximation of pi

print("Approximation of pi:", approx_pi)
print("Actual value of pi:", math.pi)
# print the approximation and the actual value of pi from the math module
# Christian Ocampo CSS 225 Module 8 lab 11/17/24


# Define the function to compare the sum of two inputs to 10
def compare_sum_to_ten():
    try:
        # Get two inputs and convert them into integers
        input1 = int(input("Enter first number: "))
        input2 = int(input("Enter second number: "))

        # Calculates the sum of the two inputs
        total = input1 + input2

        # Compare the sum with 10
        if total > 10:
            print("The sum is greater than 10.")
        elif total < 10:
            print("The sum is less than 10.")
        else:
            print("The sum is equal to 10.")
    except ValueError:
        print("Please enter valid numbers.")

# Calls the function and prints the result
compare_sum_to_ten()
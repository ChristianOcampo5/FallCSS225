# Christian Ocampo CSS 225 Module lab 8 11/17/24


# Define the function to check if 5 is in the list or not
def check_for_five(input_list):
    if 5 in input_list:
        print("The value 5 is in the list.")
    else:
        print("The value 5 is not in the list.")

# Example usage of the function
example_list = [1, 2, 3, 4, 5, 6]
check_for_five(example_list)  # Should print that 5 is in the list

another_list = [10, 20, 30]
check_for_five(another_list)  # Should print that 5 is not in the list
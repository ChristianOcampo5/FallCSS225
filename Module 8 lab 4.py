# Christian Ocampo CSS 225 Module 8 lab 11/17/24


# Define a function to check for a leap year
def is_leap_year(year):

# Determine whether a given year is a leap year.

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # year (int): The year to check.
        return True
    return False # True if the year is a leap year, False otherwise.

# Example usage of the function for the years given
year1 = 2024
year2 = 1900
year3 = 2000


# Prints the true or false on the leap years
print(f"Is {year1} a leap year? {is_leap_year(year1)}")  # True
print(f"Is {year2} a leap year? {is_leap_year(year2)}")  # False
print(f"Is {year3} a leap year? {is_leap_year(year3)}")  # True
# Christian Ocampo 10/13/2024 Lab 3

def calculate_return_day(starting_day, vacation_length):

    return_day = (starting_day + vacation_length) % 7
    return return_day

def main():

    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    starting_day = int(input("Enter the starting day number (0=Sunday, 6=Saturday): "))
    vacation_length = int(input("Enter the length of the vacation (number of nights):" ))

    return_day_number = calculate_return_day(starting_day, vacation_length)

    print(f"You will return on day {return_day_number}, which is {days_of_week[return_day_number]}")
# Christian Ocampo CSS 225 Team assignment 2 10/29/2024

#The correct number if guessed correctly
number = 9

#The options that are given for user to guess
guessed_number = int(input("Please guess a number between 1 and 10: "))

while continue_playing:

continue_playing = True


#If the correct number is guessed incorrectly
if guessed_number > 10:
    print("Invalid choice!")

#If the number is guessed correctly
elif guessed_number == number:
    print("Good guess!")

#If the number is guessed incorrectly
elif guessed_number < number:
    print("Guess higher!")

#If the number is guessed incorrectly
elif guessed_number > number:
    print("Guess lower!")

#If a number outside the given choices is entered
else:
    print("Invalid choice!")

play_again = input("Do you want to play again?" (yes/no): " .strip().lower())
if play_again = "yes":
    print("Thanks for playing")
    break
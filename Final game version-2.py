"""
Author: Christian Ocampo
Date: 12/07/2024

Game description:

This is a text based game, the player gets six options to choose from in the menu provided:

1. Go to the left of the path
2. Go to the right of the path
3. Explore the forest to find items
4. Quit game

Option 1 - Player will have the option to go to the left path that will take them to the correct path that leads to chapter two

Option 2 - Player wil have the option to go to the right path that will take them to the wrong path and loop back to the path choices

Option 3 - Explore the forest to pick up an item that would be added to the player's inventory

Option 4 - The game will terminate with an appropriate message.

"""
# Start of the chapter with four different choices to make
def chapter_one(player):
    print("\n--- Chapter One: The Forked Road ---")
    while True:
        print("\nYou emerge from a temple in the mountains and find yourself at a forked road.")
        print("1. Take the left path")
        print("2. Take the right path")
        print("3. Explore the forest")
        print("4. Exit the game")

        # Four choices have different outcomes and will print the results
        choice = input("What do you want to do? ")
        if choice == "1": # Left path takes player to the correct path to start chapter two
            print("You take the left path, but it leads to a far-off land. After 5 minutes, which leads to a small town where the next chapter starts.")
        elif choice == "2": # The wrong path puts the player back to the fork road to redo their original choice
            print("You take the right path, but it leads to a far-off land. After five minutes, player turns back and returns to the fork road.")
            print("This path leads you to Chapter Two!") # Game will inform player of game starting a new chapter
            return
        elif choice == "3":
            print("You explore the forest and find two gold coins!")
            player.add_to_inventory("gold coin")
        elif choice == "4":
            print("Thanks for playing the Adventure Game!")
            exit()
        else:
            print("Invalid choice. Try again.")

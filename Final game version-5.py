"""
Author: Christian Ocampo
Date: 12/07/2024

Game description:

This is a text based game, the player gets six options to choose from in the menu provided:

1. Explore the seashore
2. Repair broken carriage
3. Crossing giant bridge
4. Quit game

Option 1 - Explore and search the seashore to collect items that will go into the player's inventory

Option 2 - Assist the coachman with the broken carriage and earn a reward for helping fix the carriage

Option 3 - Player can decide to cross the giant bridge to proceed to chapter five

Option 4 - The game will terminate with an appropriate message.

"""

# Four different options player can choose that will print the results
def chapter_four(player):
    print("\n--- Chapter Four: The Bridge and the Shore ---")
    while True:
        print("\nYou reach the shore.")
        print("1. Search the shore for pearls")
        print("2. Help a broken carriage to earn gold")
        print("3. Cross the giant bridge to proceed to the final chapter")
        print("4. Exit the game")


        # Four options that will lead to different outcomes
        choice = input("What do you want to do? ")
        if choice == "1":
            print("You search the shore and find some pearls!")
            player.add_to_inventory("pearl")
        elif choice == "2":
            print("You help a broken carriage and the coachman gives you some gold as thanks.") # Player gets rewarded with the most gold in this job
            player.add_to_inventory("20 gold coins")
        elif choice == "3": # Player can choose to quickly proceed to the next chapter without doing side quests
            print("You cross the giant bridge and proceed to the final chapter!")
            return
        elif choice == "4":
            print("Thanks for playing the Adventure Game!")
            exit()
        else:
            print("Invalid choice. Try again.")
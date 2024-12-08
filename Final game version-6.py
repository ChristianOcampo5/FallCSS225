"""
Author: Christian Ocampo
Date: 12/07/2024

Game description:

This is a text based game, the player gets six options to choose from in the menu provided:

1. Explore the city to take on guild jobs
2. Talk to the city folk for jobs
3. Talk to the city royal official
4. Quit game

Option 1 - Explore the city of the capital to find the guild hall to take on more challenging jobs for great rewards

Option 2 - Approach a city person to take on a small job for a small reward

Option 3 - Talk to the royal official to take on a main quest to defeat the rouge knight and to conclude the game

Option 4 - The game will terminate with an appropriate message.

"""
# Add the important random to connect the chapters
import random


# Four options the player can choose to proceed the chapter
def chapter_five(player):
    """
    Chapter Five: The Royal Capital
    This function handles the logic for the royal capital and allows players to choose their actions.

    Args:
        player (Character): The player's character object.
    """

    # Four different options with outcomes that will print the results
    print("\n--- Chapter Five: The Royal Capital ---")
    while True:
        print("\nYou arrive at the royal capital.")
        print("1. Explore the city square for guild quests")
        print("2. Talk to a city person for small quests")
        print("3. Speak to the royal official to take on the main quest (defeat the rogue knight)")
        print("4. Exit the game?")

        # Four options that player can choose before going to the final stage of the game
        choice = input("What do you want to do? ")
        if choice == "1":
            print("You take on big quests from the guild and earn rewards!")
            player.add_to_inventory("10 gold coins")
        elif choice == "2":
            print("You complete small quests from city folks.")
            player.add_to_inventory("5 gold coins")
        elif choice == "3":
            print("The royal official in the city square gives you a quest to defeat the rogue knight!")
            fight_rogue_knight(player) # This option will lead to the last part of the game before ending
            return
        elif choice == "4":
            print("Exiting Chapter Five...")
            return
        else:
            print("Invalid choice. Try again.")

# A separate section of the game fighting the knight before game is completed
def fight_rogue_knight(player):
    """
    Handles the final battle with the rogue knight.


1. Explore the cave hideout
2. Proceed to fight the rouge knight
3. Quit game

Option 1 - Explore the cave to find gems that will be added to the player's inventory

Option 2 - Go forward to fight the rouge knight and defeat him to finish the game as the game coes to an end

Option 3 - The game will terminate with an appropriate message.

    Args:
        player (Character): The player's character object.
    """

    # Three options player can choose as the last part of the game
    print("\n--- The Final Battle: Rogue Knight ---")
    while True:
        print("\nYou face the rogue knight in his cave hideout.")
        print("1. Explore the cave for gems")
        print("2. Fight the rogue knight")
        print("3. Exit the game?")

        # Three options player can choose to either decide to fight the knight or hold off on the fight
        choice = input("What do you want to do? ")
        if choice == "1":
            print("You explore the cave and find rare gems!")
            player.add_to_inventory("gem")
        elif choice == "2": # The final quest of the game starts as the main quest is initiated
            print("You come across the rogue knight as he readies for combat.")
            print("You fight the rogue knight and defeat him!")
            print("Congratulations! You have completed the adventure game!") # The game congratulates player for finishing the game
            return
        elif choice == "3":
            print("Exiting the battle...") # The game comes to an end after ever chapter is completed
            return
        else:
            print("Invalid choice. Try again.")
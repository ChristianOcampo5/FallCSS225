"""
Author: Christian Ocampo
Date: 12/07/2024

Game description:

This is a text based game, the player gets six options to choose from in the menu provided:

1. Explore the forest
2. Fight the bear
3. Exit the game


Option 1 - Explore the forest to gather items into the player's inventory

Option 2 - Fight the bear in an intense battle that will lead to chapter four after the bear is defeated

Option 3 - The game will terminate with an appropriate message.

"""
# Important the random for the game to pull other chapters
import random


# Three options that the player can select
def chapter_three(player):
    print("\n--- Chapter Three: The Forest ---")
    while True:
        print("\nYou are in the forest. You have two choices:")
        print("1. Explore the forest further")
        print("2. Fight a bear to proceed to Chapter Four")
        print("3. Exit the game")


        # Three different options with their own outcomes that will print the results
        choice = input("What do you want to do? ")
        if choice == "1":
            print("You explore the forest and find useful items!")
            found_item = random.choice(["herbs", "magic stone", "gold coin"])
            player.add_to_inventory(found_item)
        elif choice == "2": # Fighting and defeating the bear will let player proceed to the next chapter
            print("You come across a spiked-back bear and engage in combat! You defeat the bear and proceed to Chapter Four.")
            player.add_to_inventory("golden dagger")
            return
        elif choice == "3":
            print("Thanks for playing the Adventure Game!")
            exit()
        else:
            print("Invalid choice. Try again.")
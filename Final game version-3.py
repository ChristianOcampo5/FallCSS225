"""
Author: Christian Ocampo
Date: 12/07/2024

Game description:

This is a text based game, the player gets six options to choose from in the menu provided:

1. Explore the forest
2. Go to the right of the path
3. Go to the left of the path
4. Quit game

Option 1 - THe guild hall is a hub for adventurers to take on challenging jobs with great rewards that the player can take on jobs for

Option 2 - The townsfolk can be approached to take on smaller jobs that give small rewards that the player can take on

Option 3 - The town mayor keeps everything in order in his town and keeps an eye on outside threat,
he will give an important job that leads to chapter three

Option 4 - The game will terminate with an appropriate message.

"""

# Four options that the player can choose from
def chapter_two(player):
    print("\n--- Chapter Two: The Town ---")
    while True:
        print("\nYou arrive in a bustling town and look around the town square for what to do next.")
        print("1. Visit the guild hall to take on a big quest")
        print("2. Talk to a townsfolk to take on a small quest")
        print("3. Speak to the town mayor for a quest leading to Chapter Three")
        print("4. Exit the game")


        # These four options have a different outcomes with printed results
        choice = input("What do you want to do? ")
        if choice == "1":
            print("You take on a big quest from the guild hall. This will prepare you for future challenges and earn good rewards!")
            player.add_to_inventory("10 gold coins")
        elif choice == "2":
            print("A townsfolk gives you a small quest, you take on a small project for a small reward.")
            player.add_to_inventory("5 gold coins")
        elif choice == "3": # main quest lets player go onto the next chapter
            print("The mayor gives you an important quest that leads to Chapter Three!")
            return
        elif choice == "4":
            print("Thanks for playing the Adventure Game!")
            exit()
        else:
            print("Invalid choice. Try again.")
"""
Author: Christian Ocampo
Date: 12/07/2024

Game description:

This is a text based game, the player gets six options to choose from in the menu provided:



"""


"""
The class Character is used to manage the player's name, health, and
inventory items. The class has methods (functions) called by the logic
in the program. 

Methods:

add_to_inventory: Adds items to the inventory list.

remove_from_inventory: Removes a used and random item from the inventory
          list.

check_inventory: prints all items in the inventory list

find_item_in_inventory: Check if an item is in the inventory

count_items: It counts the number of a given item in inventory

"""

# The class system in place to let user add a name for the character with a health and an inventory bag
class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item} has been removed from your inventory.")
        else:
            print(f"{item} not found in inventory.")

    def check_inventory(self):
        if self.inventory:
            print("Your inventory contains:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")

    # Allows player to find items and be put into their inventory
    def find_item_in_inventory(self, item):
        if item in self.inventory:
            print(f"You have {item} in your inventory.")
        else:
            print(f"{item} is not in your inventory.")

    def count_item(self, item):
        count = self.inventory.count(item)
        print(f"You have {count} of {item}.")
# Christian Ocampo CSS 225 Module 8 11/17/24


# Using the self function for the character
class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses


# Create a player instance
player1 = Character('', '', '')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']

# Print player's weapons and weaknesses
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

# Function to check if the character can perform tasks
def check_tasks(character):
    tasks = {
        "Climb a mountain": {
            "required_items": ['rope', 'coat', 'first aid kit'],
            "restricted_debuffs": ['slow']
        },
        "Cook a meal": {
            "required_items": ['pan', 'groceries'],
            "restricted_debuffs": ['small']
        },
        "Write a book": {
            "required_items": ['pen', 'paper', 'idea'],
            "restricted_debuffs": ['confusion']
        },
    }
# Checks the tasks ton what can be performed and not be performed
    for task, requirements in tasks.items():
        print(f"\nChecking if '{character.nickname}' can perform task: {task}")
        missing_items = [item for item in requirements['required_items'] if item not in character.weapons]
        has_restricted_debuffs = any(debuff in character.weaknesses for debuff in requirements['restricted_debuffs'])

# If functions to give tasks to each scenario
        if missing_items:
            print(f"Cannot perform task '{task}': Missing items: {missing_items}")
        elif has_restricted_debuffs:
            print(f"Cannot perform task '{task}': Has restricted debuffs: {requirements['restricted_debuffs']}")
        else:
            print(f"Task '{task}' can be performed successfully!")

# Run the check for player1
check_tasks(player1)
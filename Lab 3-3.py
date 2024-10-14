# Christian Ocampo 10/13/2024 Lab 3


allowed_users = ['Christian', 'Mr. Tovar']

def greet_user(name):
    if name in allowed_users:
        print(f"hello, {name}.")
    else:
        print(f"invalid, {'Christian', 'Mr. Tovar',}.")
# --- Show drawing options to the user---
def print_menu():
    print("\nHow would you like to draw your Pokémon? ")
    print("1. Random")
    print("2. By ID")
    print("3. By Name")
    print("4. Exit")


# --- Printing Pokémon info (ui) ---
def print_pokemon(pokemon):
    print("\n🎯 Pokémon Drawn:")
    print(f"Name   : {pokemon['name'].title()}")
    print(f"ID     : {pokemon['id']}")
    print(f"Height : {pokemon['height']}")
    print(f"Weight : {pokemon['weight']}")
    print(f"Types  : {', '.join(pokemon['types'])}\n")

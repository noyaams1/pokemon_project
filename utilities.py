from constant_vars import DB_PATH
from ui_messages import print_pokemon
from json_functions import save_json
from api import get_all_pokemon_data , get_pokemon_details_from_api
import random

# --- checking if pokemon is already in DB, if not: adding it.
def update_db_if_needed(db, details):
    name = details["name"]
    if name in db:
        print(f"Pokémon {name} is already in your collection!")
        print_pokemon(db[name])
        return True
    else:
        print(f"🎲 Adding new Pokémon: {name}")
        db[name] = details
        save_json(db, DB_PATH)
        print_pokemon(details)
        return False

# --- Random drawing---
def random_choice(db):
    all_pokemon = get_all_pokemon_data()
    if not all_pokemon:
        print("Error loading Pokémon list.")
        return

    chosen = random.choice(all_pokemon)["name"]
    details = get_pokemon_details_from_api(chosen)
    if details:
        update_db_if_needed(db, details)

# --- Drawing pokemon by ID ---
def drawing_by_id(db):
    poke_id = input("Enter Pokémon ID (e.g., 25): ").strip()
    if not poke_id.isdigit():
        print("Please enter a valid number.")
        return

    poke_id = int(poke_id)
    db_by_id = {p["id"]: p for p in db.values()}
    if poke_id in db_by_id:
        print("✅ Found in database!")
        print_pokemon(db_by_id[poke_id])
    else:
        details = get_pokemon_details_from_api(poke_id)
        if details:
            update_db_if_needed(db, details)


# --- Drawing pokemon by name ---
def drawing_by_name(db):
    name = input("Enter Pokémon name (e.g., pikachu): ").strip().lower()
    if name in db:
        print("✅ Found in database!")
        print_pokemon(db[name])
    else:
        details = get_pokemon_details_from_api(name)
        if details:
            update_db_if_needed(db, details)



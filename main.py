from constant_vars import DB_PATH
from json_functions import load_json
from utilities import random_choice, drawing_by_id, drawing_by_name
from ui_messages import print_menu


# --- Running the program---
def main():
    db = load_json(DB_PATH)
    while True:
        print_menu()
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            random_choice(db)
        elif choice == "2":
            drawing_by_id(db)
        elif choice == "3":
            drawing_by_name(db)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("Please choose a valid option (1-4).")


if __name__ == "__main__":
    main()

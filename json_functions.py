import json
import os


# --- General JSON functions ---
def save_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def load_json(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                content = f.read().strip()
                if not content:
                    return {}  # empty db file return an empty object
                return json.loads(content)
        except json.JSONDecodeError:
            print("⚠️ JSON file is corrupted or invalid. Starting with empty database.")
            return {}
    return {}

# 🐾 Pokémon Fetcher – Using PokeAPI + JSON

A console-based Python app that lets you fetch random Pokémon from the [PokeAPI](https://pokeapi.co/), store them in JSON, and view their details. Includes optional AWS deployment for a hosted EC2-based version.

---

## 🚀 Features

- 🧠 Fetches random Pokémon from the PokeAPI
- 🗂️ Saves Pokémon data to a local JSON file (avoids duplicates)
- 📊 Displays Pokémon stats, types, and height/weight
- 💾 Persistent storage via JSON
- ☁️ Deployment-ready with AWS EC2 provisioning

---

## 📥 Download & Setup

1. Clone the repo:

```bash
git clone https://github.com/noyaams1/pokemon_project.git
cd pokemon-project
```

2. Install dependencies (optional):
```bash
pip install -r requirements.txt

```
Note: 
- Make sure your AWS CLI is configured.
- Create a key pair in AWS and import your public key.
- Port 22 is opened publicly for SSH access to the ec2 app server.

3. Run the app:
```bash
python main.py

```

---

## 🗃️ Example JSON schema

```json
{
  "pikachu": {
    "id": 25,
    "height": 4,
    "weight": 60,
  "types": ["electric"]
  }
}
```

---


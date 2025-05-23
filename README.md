# 🐾 Pokémon Fetcher – Using PokeAPI + JSON

A console-based Python application that lets you fetch random Pokémon from the [PokeAPI](https://pokeapi.co/), store them in JSON format, and view their details. Includes optional AWS deployment for a hosted EC2-based version.

---

## 🚀 Features

- 🧠 **Smart Fetching**: Retrieves random Pokémon from the comprehensive PokeAPI
- 🗂️ **JSON Storage**: Saves Pokémon data locally with automatic duplicate prevention
- 📊 **Rich Display**: Shows detailed stats, types, abilities, height, and weight
- 💾 **Persistent Data**: Maintains your Pokémon collection across sessions
- ☁️ **Cloud Ready**: One-click AWS EC2 deployment with automated provisioning
- 🎯 **Interactive Console**: User-friendly command-line interface

---

## 📥 Download & Setup

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/noyaams1/pokemon_project.git
   cd pokemon_project
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   *Required packages:*
   - `requests` - For API calls
   - `json` - Data storage (built-in)
   - `random` - Random Pokémon selection (built-in)

3. **Run the application:**
   ```bash
   python main.py
   ```

### Prerequisites

- **Python 3.7+** installed on your system
- **AWS CLI configured** (for deployment only)
  

## 🗃️ Data Structure

### JSON Schema Example

```json
{
  "pikachu": {
    "id": 25,
    "name": "pikachu",
    "height": 4,
    "weight": 60,
    "types": ["electric"]
    },
  "charizard": {
    "id": 6,
    "name": "charizard",
    "height": 17,
    "weight": 905,
    "types": ["fire", "flying"]
}
}
```

## ☁️ Deploy on AWS EC2 (Optional)

Transform your console app into a cloud-hosted service with our automated deployment script.

### Prerequisites for Deployment

1. **AWS CLI Configuration:**
   ```bash
   aws configure
   # Enter your AWS Credentials
   ```

2. **Create EC2 Key Pair:**
   - Log into AWS Console → EC2 → Key Pairs
   - Create new key pair or import your existing public key
   - Download the `.pem` file and store it securely

3. **Verify Permissions:**
   Ensure your AWS account has permissions for:
   - EC2 instance creation and management
   - Security group creation and modification
   - VPC access

### Deployment Steps

1. **Run the deployment script:**
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

2. **What the script does:**
   - 🚀 Launches a new EC2 instance in `us-west-2` (Amazon Linux 2)
   - 🔧 Installs Python 3, pip, Git, and system dependencies
   - 📦 Clones your GitHub repository automatically
   - 🔌 Installs all Python requirements
   - 🎯 Configures the app to auto-run on system startup
   - 🔒 Sets up security group with SSH access (port 22)

3. **Access your cloud instance:**
   ```bash
   ssh -i your-key-pair.pem ec2-user@[INSTANCE-IP]
   cd pokemon_project
   python main.py
   ```

### Deployment Configuration

The deployment creates:
- **Instance Type**: t2.micro (AWS Free Tier eligible)
- **Operating System**: Amazon Linux 2
- **Storage**: 8GB General Purpose SSD
- **Network**: Default VPC with public IP
- **Security**: SSH access on port 22



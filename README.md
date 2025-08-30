
# Doc The Tiger Chatbot

#### This project is a simple chatbot that leverages OpenAI API keys to create a chatbot that acts like the Towson University campus mascot and encourages students to join the newly forming A.I club. Instructions for running the chatbot locally are below.


## 1. Clone the Repository
```bash
git clone https://github.com/BrendanHodges/DOC_THETIGER.git
cd DOC_THETIGER
```

---

## 2. Create a Virtual Environment
It’s recommended to use a virtual environment so dependencies stay project-specific.

```bash
# Create a virtual environment named .venv
python -m venv .venv
```

---

## 3. Activate the Virtual Environment
**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows (PowerShell or Git Bash):**
```bash
.venv\Scripts\activate
```

---

## 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 5. Setting Up Your API Key

This project requires an API key to access certain services. Follow these steps:

### Get an API Key
1. Create an account with the API provider (for example, [OpenAI](https://platform.openai.com/) if you're using their API).
2. Generate a new API key from your account dashboard.
3. Copy the API key.

### Create a `.env` File
In your project's root directory, create a file named `.env`:
```bash
touch .env
```

### Add Your API Key
Inside `.env`, add your API key like this:
```
API_KEY=your_api_key_here
```

⚠️ **Important:** Never commit this `.env` file to GitHub. Add `.env` to your `.gitignore`.

### Load the API Key in Python
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
```

---

## ▶️ 6. Run the Program

```bash
python main.py
```

---

## 🛑 7. Deactivate When Done

```bash
deactivate
```

---

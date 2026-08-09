# 🤖 Streamlit Chatbot

A simple **rule-based chatbot** built with **Python** and **Streamlit**. The bot matches a user's message against a dictionary of predefined questions and returns the corresponding response through a clean web interface.

This is a beginner-friendly project that demonstrates the fundamentals of building an interactive web app, handling user input, and managing state in Streamlit.

---

## ✨ Features

- 🧠 **Rule-based responses** — answers 60+ predefined questions (greetings, jokes, FAQs, general knowledge, and more)
- 🌐 **Web interface** — clean, browser-based UI powered by Streamlit
- 🔡 **Case-insensitive matching** — input is normalized to lowercase before lookup
- 💬 **Fallback response** — politely asks the user to rephrase when no match is found
- ⚡ **Lightweight** — no external APIs, no database, runs entirely in Python

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language  | Python 3.8+ |
| Framework | Streamlit  |
| Logic     | Dictionary-based response mapping |

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shivansh-sa/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit
   ```

---

## 🚀 Usage

Run the app from the project directory:

```bash
streamlit run app.py
```

> Replace `app.py` with the actual name of your Python file if it's different.

Streamlit will open the chatbot in your default browser (usually at `http://localhost:8501`). Type a message in the input box and click **Send** to chat.

---

## 🧩 How It Works

The chatbot logic is built around three simple pieces:

1. **A `responses` dictionary** — maps each expected user question (the *key*) to a fixed answer (the *value*).
2. **`get_chatbot_response()`** — converts the input to lowercase, looks it up in the dictionary, and returns either the matched answer or a fallback message.
3. **`main()`** — renders the Streamlit UI: a title, a text input, and a **Send** button that displays both the user's message and the bot's reply.

```python
def get_chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm sorry, I don't understand that. Could you please rephrase?"
```

---

## 💡 Example Queries

Try asking the bot:

- `hello`
- `tell me a joke`
- `what's the capital of France?`
- `how do I reset my password?`
- `what payment methods do you accept?`

---

## 🔧 Customizing the Bot

Adding a new response is as easy as adding a key–value pair to the `responses` dictionary:

```python
responses = {
    # ... existing responses ...
    "what is streamlit?": "Streamlit is an open-source Python framework for building data apps.",
}
```

Keep the **key in lowercase** so it matches the normalized input.

---

## ⚠️ Limitations

- **Exact-match only** — the bot only responds when the input *exactly* matches a dictionary key. "hi there" won't match "hi".
- **No natural language understanding** — it can't handle typos, synonyms, or rephrased questions.
- **Static answers** — some responses (e.g. time, current officials) are hardcoded and may become outdated.

---

## 🔮 Future Improvements

- Add **fuzzy matching** (e.g. `difflib` or `fuzzywuzzy`) to handle typos and near-matches
- Maintain a **chat history** so the conversation scrolls like a real messenger
- Integrate an **NLP model or LLM API** for open-ended, dynamic conversations
- Add **keyword-based matching** instead of exact-match lookup

---

## 👤 Author

**Shivansh Srivastava**
🔗 GitHub: [github.com/Shivansh-sa](https://github.com/Shivansh-sa)

---

⭐ *If you found this project helpful, consider giving it a star on GitHub!*

import tkinter as tk
import json
import random
import re

# Load intents
with open('intents.json') as f:
    intents = json.load(f)

# Function to generate response
def get_response(user_input):
    user_input = user_input.lower()
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern in user_input:
                return random.choice(intent['responses'])
    return "I'm not sure I understand. Try asking something else."

# Function to update chat window
def send_message():
    user_input = entry_box.get()
    if user_input.strip() == "":
        return
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    response = get_response(user_input)
    chat_log.insert(tk.END, "SmartBot: " + response + "\n\n")
    chat_log.config(state=tk.DISABLED)
    entry_box.delete(0, tk.END)

# Setup GUI
root = tk.Tk()
root.title("SmartBot - AI Chatbot")
root.geometry("400x500")
root.configure(bg="white")

chat_log = tk.Text(root, bg="white", fg="black", font=("Arial", 12))
chat_log.config(state=tk.DISABLED)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry_box = tk.Entry(root, font=("Arial", 12))
entry_box.pack(padx=10, pady=(0, 10), fill=tk.X, side=tk.LEFT, expand=True)

send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(padx=(0, 10), pady=(0, 10), side=tk.RIGHT)

root.mainloop()
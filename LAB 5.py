import re

rules = {
    "hello": "Hello! How can I help you?",
    "hi": "Hello! How can I help you?",
    "how are you": "I am fine. Thank you!",
    "your name": "My name is SimpleBot.",
    "who are you": "I am a simple rule-based chatbot.",
    "help": "I can answer simple questions.",
    "artificial intelligence": "AI is the simulation of human intelligence in machines.",
    "thanks": "You are welcome!",
    "bye": "Goodbye! Have a nice day!"
}

def chatbot(user):
    user = user.lower()

    for key, value in rules.items():
        if re.search(key, user):
            return value

    return "Sorry, I don't understand."

print("===== SIMPLE CHATBOT =====")
print("Type bye to exit.")

while True:
    user = input("You: ")
    print("Bot:", chatbot(user))

    if re.search("bye", user.lower()):
        break

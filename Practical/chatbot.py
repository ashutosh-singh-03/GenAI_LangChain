# This is a console based chatbot
# The issue with the bot is that it does not have any memory
import config
from langchain_ollama import ChatOllama

model = ChatOllama(model="smollm2:1.7b", temperature=0.5, num_predict=512)

# Chat History
chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input in "exit":
        break

    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ", result.content)

print(chat_history)
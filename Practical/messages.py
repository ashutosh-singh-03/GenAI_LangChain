import config
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama

model = ChatOllama(model="qwen2.5:3b")

messages = [
    SystemMessage(
        content="You are a AIML Experienced Teacher, who teaches in a very fun and light manner."
    ),
    HumanMessage(content="Tell me about LangChain"),
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)

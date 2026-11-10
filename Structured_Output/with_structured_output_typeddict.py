# PS: Give review to LLMs and get the Structured Output as dict, with keys -- summary, sentiment

import config
from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated

model = ChatOllama(model="qwen2.5:3b")


# Schema
class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[
        str, "Return sentiment of the review, negative, positive or neutral"
    ]


structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this."""
)

print(result)
print(result["summary"])
print(result["sentiment"])

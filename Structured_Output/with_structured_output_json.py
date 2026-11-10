# PS: Give review to LLMs and get the Structured Output as dict, with keys -- summary, sentiment

import config
from langchain_ollama import ChatOllama
from typing import (
    TypedDict,
    Annotated,
    Optional,
    Literal,
)  # Literal is used to give external options which is given as result by the model

model = ChatOllama(model="qwen2.5:3b")


# Schema
json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "description": "Write down all the key themes discussed in the review in a list.",
            "items": {"type": "string"},
        },
        "summary": {"type": "string", "description": "A brief summary of the review"},
        "sentiment": {
            "type": "string",
            "description": "Return sentiment of the review, negative, positive or neutral",
            "enum": ["Pos", "Neg"],
        },
        "pros": {
            "type": ["array", "null"],
            "description": "Write down all the pros inside a list.",
            "items": {"type": "string"},
        },
        "cons": {
            "type": ["array", "null"],
            "description": "Write down all the cons inside a list.",
            "items": {"type": "string"},
        },
        "name": {
            "type": ["string", "null"],
            "description": "Write the name of the reviewer.",
        },
    },
    "required": ["key_themes", "summary", "sentiment"],
}


structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke(
    """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning-fast, whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day, even with heavy use, and the 45W fast charging is a lifesaver.

    The S Pen integration is a great touch for note-taking and quick sketches, although I don't use it very often. What really blew me away is the 200MP camera. The night mode is stunning, capturing crisp and vibrant images even in low-light conditions. The 100x zoom can be useful for distant objects, but image quality starts to noticeably decline beyond 30x zoom.

    However, the phone's size and weight make it somewhat uncomfortable for one-handed use. In addition, Samsung's One UI still comes with its share of bloatware. I don't really need multiple Samsung apps for services that Google already provides. The $1,300 price tag is also difficult to justify for many buyers.

    Pros
    Insanely powerful processor, ideal for gaming and productivity
    Stunning 200MP camera with impressive zoom capabilities
    Excellent battery life with fast charging support
    S Pen support is unique and genuinely useful

    Cons
    Bulky and heavy, making one-handed use difficult
    One UI still includes unnecessary pre-installed apps (bloatware)
    Expensive compared to many competitors
    
    Written by Ashutosh Singh
    """
)

print(result)
print(result["summary"])
print(result["sentiment"])

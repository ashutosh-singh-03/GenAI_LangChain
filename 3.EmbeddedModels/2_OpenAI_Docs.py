from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

document = [
    "Delhi is the capital of India.",
    "Kolkata is the capital of West Bengal.",
    "Narendra Modi is the Prime Minister of India.",
]

result = model.embed_documents(document)  # Returns a 2D list of all the vectors
print(str(result))

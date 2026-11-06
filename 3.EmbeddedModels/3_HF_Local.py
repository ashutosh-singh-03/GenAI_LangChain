from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["HF_HOME"] = os.getenv("HF_HOME")

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

document = [
    "Delhi is the capital of India.",
    "Kolkata is the capital of West Bengal.",
    "Narendra Modi is the Prime Minister of India.",
]

result = embedding.embed_documents(document)
print(str(result))

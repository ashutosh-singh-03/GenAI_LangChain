from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["HF_HOME"] = os.getenv("HF_HOME")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers.",
]

query = "Tell me about bumrah."

doc_embedding = embedding.embed_documents(documents)  # returns a 2D List
query_embedding = embedding.embed_query(query)  # returns a list

scores = cosine_similarity([query_embedding], doc_embedding)[0]

index, score = sorted(enumerate(scores), key=lambda x: x[1])[-1]

print(index, score)
print(f'User Query: "{query}"')
print(documents[index])
print("Similarity Score is: ", score)

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["HF_HOME"] = os.getenv("HF_HOME")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
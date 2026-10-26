import os

from dotenv import load_dotenv
from google import genai

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

text = "You are a developer"

response = client.models.embed_content(model="gemini-embedding-001", contents=text)

embedding = response.embeddings[0].values

print("Text:", text)
print("Vector dimensions:", len(embedding))
print("Embedding:", embedding)

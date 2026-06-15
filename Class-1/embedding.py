from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

text = "Eiffel Tower is in Paris and is a famous landmark, it is 324 meters tall"

response = client.embeddings.create(
    input=text,
    model="text-embedding-3-small"
)

print("Vector Embedding:")
print(response.data[0].embedding)

# ==========================================
# EMBEDDING GENERATION ALGORITHM
# ==========================================

# Step 1: Load environment variables from .env file

# Step 2: Create OpenAI client

# Step 3: Take input text from user/application

# Step 4: Send text to embedding model
#         (text-embedding-3-small)

# Step 5: Model tokenizes the text

# Step 6: Tokens are converted into token IDs

# Step 7: Token IDs pass through Transformer layers

# Step 8: Transformer generates a dense vector
#         representation (Embedding)

# Step 9: Receive embedding vector response

# Step 10: Print/store embedding vector
#==============================================================================
'''Input Text
     ↓
Tokenization
     ↓
Token IDs
     ↓
Embedding Model
     ↓
Transformer Layers
     ↓
Vector Embedding
     ↓
Output Vector'''
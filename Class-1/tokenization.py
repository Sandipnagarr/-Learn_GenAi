import tiktoken

# Step 1: Load tokenizer
enc = tiktoken.encoding_for_model("gpt-4o")

# Step 2: Input text
text = "i live in noida since my gradution time"

# Step 3: Tokenize and Encode
token_ids = enc.encode(text)

# Step 4: Print token IDs
print("Encoded Token IDs:", token_ids)

# Step 5: Count tokens
print("Token Count:", len(token_ids))

# Step 6: Decode back to text
decoded_text = enc.decode(token_ids)

print("Decoded Text:", decoded_text)

'''Input Text
     ↓
Load Tokenizer
     ↓
Tokenization
     ↓
Tokens
     ↓
Token Encoding
     ↓
Token IDs
     ↓
Token Count
     ↓
LLM Processing'''
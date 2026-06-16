# Import the OpenAI library
from openai import OpenAI

# Create an OpenAI client instance
# Make sure your OPENAI_API_KEY is set in environment variables
client = OpenAI()

# Send a chat completion request to the model
response = client.chat.completions.create(
    model="gpt-4o",  # Model to use

    # Conversation messages sent to the model
    messages=[
        {
            "role": "user",
            "content": """
Input: Apple
Output: Fruit

Input: Carrot
Output: Vegetable

Input: Mango
Output:
"""
        }
    ]
)

# Extract and print the model's response
# The model learns the pattern:
# Apple -> Fruit
# Carrot -> Vegetable
# Therefore it predicts:
# Mango -> Fruit
print(response.choices[0].message.content)
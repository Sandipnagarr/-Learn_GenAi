# Import OpenAI library
from openai import OpenAI

# Create OpenAI client
client = OpenAI()

# Send request to GPT model
response = client.chat.completions.create(
    model="gpt-4o",

    messages=[
        {
            "role": "system",

            # ROLE PROMPTING:
            # Assigns a specific role/job to the AI.
            # Here the AI behaves like a Python Developer.
            "content": "Act as a Python Developer."
        },
        {
            "role": "user",

            # User's question
            "content": "Explain decorators."
        }
    ]
)

# Print the AI response
print(response.choices[0].message.content)
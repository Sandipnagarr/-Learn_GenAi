# Import OpenAI library
from openai import OpenAI

# Create OpenAI client
client = OpenAI()

# Send request to GPT model
response = client.chat.completions.create(
    model="gpt-4o",
    temperature=4.5,

    messages=[
        {
            "role": "system",

            # PERSONA PROMPTING:
            # Defines a complete identity for the AI.
            # Includes:
            # - Role
            # - Experience
            # - Personality
            # - Communication style
            # - Expertise

            "content": """
            You are a Senior Python Architect with 15 years of experience.

            Your characteristics:
            - Explain concepts clearly
            - Use real-world examples
            - Follow industry best practices
            - Mentor junior developers
            """
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

def greet():
 print("hello india")
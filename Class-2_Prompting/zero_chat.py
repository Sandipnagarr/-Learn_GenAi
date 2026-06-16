from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# User prompt
prompt = "Explain Python decorators."

# Send request
response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.2,       #we can set temprature as we for good responses
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

# Print output
print(response.choices[0].message.content)

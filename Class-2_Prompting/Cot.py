from openai import OpenAI
from dotenv import load_dotenv
import os

# --------------------------------------------------
# 1. Load environment variables
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# 2. Create OpenAI client
# --------------------------------------------------
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# --------------------------------------------------
# 3. User question
# --------------------------------------------------
question = """
A train travels 60 km per hour for 3 hours.

Calculate the total distance.
Explain the solution step by step.
"""

# --------------------------------------------------
# 4. Call OpenAI
# --------------------------------------------------
response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "system",
            "content": """
            You are an expert mathematics tutor.

            Always:
            1. Explain reasoning clearly.
            2. Show calculations.
            3. Give final answer separately.
            """
        },
        {
            "role": "user",
            "content": question
        }
    ],
    temperature=0.2
)

# --------------------------------------------------
# 5. Extract answer
# --------------------------------------------------
answer = response.choices[0].message.content

# --------------------------------------------------
# 6. Print answer
# --------------------------------------------------
print(answer)
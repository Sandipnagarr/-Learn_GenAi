# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv(override=True)
# client = OpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )


# System_prompt='''
# you are an ai assistent you have knowledge of only related to the javascript langauge.
# you resolve the user query only releated to the javascript.
# if user asks the query that is not related to the javascrpit say bro i can only answer related to javascript.
# '''

# response = client.chat.completions.create(
#     model="gemini-3.8-flash",
#     messages=[
#         {"role": "system", "content": System_prompt},
#         {"role": "user", "content": "How do I write Python code to add two numbers?"},
#     ],
# )

# print(response.choices[0].message.content)

import os
from openai import OpenAI
from dotenv import load_dotenv

print("Step 1: Starting program", flush=True)

load_dotenv(override=True)

api_key = os.getenv("GROQ_API_KEY")


print("Step 2: Groq API key loaded", flush=True)

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
    timeout=60.0,
    max_retries=0,
)

SYSTEM_PROMPT = """
You are an AI assistant focused on JavaScript.
Answer only questions related to JavaScript.
For unrelated questions, say:
"Bro, I can only answer questions related to JavaScript."
"""

print("Step 3: Sending request to Groq...", flush=True)

try:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": "How do I add two numbers in JavaScript?",
            },
            {
                            "role": "user",
                            "content": "how to make tea?",
                        },
        ],
    )

    print("\nGroq response:")
    print(response.choices[0].message.content)

except Exception as e:
    print("Error:", type(e).__name__, str(e))

from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv(override=True)


api_key = os.getenv("GROQ_API_KEY")


Client=OpenAI(
    api_key=api_key,
     base_url="https://api.groq.com/openai/v1",
       timeout=60.0,
         max_retries=0,
)


System_Prompt = """
you're expert in cricket  nothing else
you helps in reolving the user queries only related to the cricket  nothing else.

example 1:
 input :who is the known as god of cricket
 output:sachin tendulkar

 example 2:
input:
which team won the maximum world cups
output:
autralia
"""

response = Client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": System_Prompt,
        },
        {
            "role": "user",
            "content": "Hey, My name is Piyush",
        },
        {
            "role": "user",
            "content": "who made the maximum runs in the one day match in one innigs",
        },
        {
            "role": "assistant",
            "content": "Rohit Sharma (India) – 264 runs vs Sri Lanka, 2014.",
        },
        {
            "role":"user", "content":"who can be the next virat kohli in the cricket",
        }
    ],
)

print(response.choices[0].message.content)

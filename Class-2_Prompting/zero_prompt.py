from dotenv import dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
prompt="explain what is api "
response=client.chat.completions.create({
    model:"chat_gpt40",
    messege=[{"role":"user","content":prompt,}]
 })
print(response.choice[0].messege.content)


let client =OpenAI()
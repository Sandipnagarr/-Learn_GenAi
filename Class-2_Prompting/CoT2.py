# -------------------------------------------------------------
# Import required libraries
# -------------------------------------------------------------

from dotenv import load_dotenv
from openai import OpenAI
import json

# -------------------------------------------------------------
# Load environment variables from .env file
# This loads OPENAI_API_KEY into the environment
# -------------------------------------------------------------

load_dotenv()

# -------------------------------------------------------------
# Create OpenAI client
# The SDK automatically reads OPENAI_API_KEY
# -------------------------------------------------------------

client = OpenAI()

# -------------------------------------------------------------
# SYSTEM PROMPT
#
# This prompt forces the model to:
# 1. Think step-by-step
# 2. Return JSON only
# 3. Follow a fixed reasoning workflow
#
# Workflow:
# analyse -> think -> validate -> result
# -------------------------------------------------------------

SYSTEM_PROMPT = """
You are a helpful AI assistant specialized in solving user queries.

For every user query:

1. Analyse the problem
2. Think about the solution
3. Validate the reasoning
4. Produce the final result

Return ONLY valid JSON.

Format:
{
    "step": "string",
    "content": "string"
}

Possible step values:
- analyse
- think
- validate
- result
"""

# -------------------------------------------------------------
# Conversation history
#
# Chat models are stateless.
# Therefore we must keep track of all messages manually.
# -------------------------------------------------------------

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

# -------------------------------------------------------------
# Get user input
# -------------------------------------------------------------

query = input("> ")

messages.append(
    {
        "role": "user",
        "content": query
    }
)

# -------------------------------------------------------------
# Main Agent Loop
#
# This loop continues until the model returns:
#
# {
#   "step":"result"
# }
#
# -------------------------------------------------------------

while True:

    # ---------------------------------------------------------
    # Call OpenAI Model
    #
    # response_format ensures JSON output
    # ---------------------------------------------------------

    response = client.chat.completions.create(
        model="gpt-4.1",
        response_format={"type": "json_object"},
        messages=messages
    )

    # ---------------------------------------------------------
    # Extract model output
    # ---------------------------------------------------------

    assistant_reply = response.choices[0].message.content

    # Store response in chat history
    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    # Convert JSON string into Python dictionary
    parsed_response = json.loads(assistant_reply)

    step = parsed_response.get("step")
    content = parsed_response.get("content")

    # ---------------------------------------------------------
    # THINK STEP
    #
    # Here you could call another model
    # (Claude, Gemini, DeepSeek, etc.)
    #
    # Then append validation result back into chat history.
    # ---------------------------------------------------------

    if step == "think":

        print("🧠 THINKING:", content)

        # Example placeholder validation
        validation = {
            "step": "validate",
            "content": "External validation completed."
        }

        messages.append(
            {
                "role": "assistant",
                "content": json.dumps(validation)
            }
        )

        continue

    # ---------------------------------------------------------
    # Intermediate Steps
    #
    # analyse
    # validate
    # ---------------------------------------------------------

    if step != "result":

        print("🧠", content)

        continue

    # ---------------------------------------------------------
    # Final Result
    # ---------------------------------------------------------

    print("🤖", content)

    break


'''User Input
     │
     ▼
System Prompt
     │
     ▼
GPT-4.1
     │
     ▼
analyse
     │
     ▼
think
     │
     ▼
validate
     │
     ▼
result
     │
     ▼
Display Final Answer'''
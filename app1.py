import os
from anthropic import Anthropic
from dotenv import load_dotenv
from prompts import system_message_Damian

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

print("API KEY FOUND:", api_key is not None)

client = Anthropic(api_key=api_key)

def run_agent(user_input):
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1500,
        system=system_message_Damian,
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return response.content[0].text


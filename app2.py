import os
from anthropic import Anthropic
from dotenv import load_dotenv
from prompts import system_message_Heather

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def run_agent(user_input, damian_convo=""):
    full_prompt = f"""
Damian conversation summary:
{damian_convo}

Current user request:
{user_input}
    """

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=system_message_Heather,
        messages=[
            {
                "role": "user",
                "content": full_prompt
            }
        ]
    )

    return response.content[0].text

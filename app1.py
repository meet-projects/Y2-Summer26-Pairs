import os
from anthropic import Anthropic
from dotenv import load_dotenv

from prompts import system_message_Damian
from pdf_tool import generate_pdf


# ==========================
# PDF TOOL DEFINITION
# ==========================

tools = [
    {
        "name": "generate_pdf",
        "description": "Creates a PDF theater guide about a musical or play.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "The name of the theater show"
                },
                "content": {
                    "type": "string",
                    "description": "The full theater guide content for the PDF"
                }
            },
            "required": [
                "title",
                "content"
            ]
        }
    }
]


# ==========================
# ANTHROPIC SETUP
# ==========================

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

print("API KEY FOUND:", api_key is not None)

client = Anthropic(api_key=api_key)


# Conversation memory
messages = []


# ==========================
# DAMIAN FUNCTION
# ==========================

def run_agent(user_input):

    # Save user message
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )


    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=3000,
        system=system_message_Damian,
        messages=messages,
        tools=tools,
        tool_choice={
            "type": "auto"
        }
    )


    # DEBUG: See what Claude returned
    print("\n========== DEBUG ==========")
    print(response.content)
    print("===========================\n")


    assistant_response = ""


    for block in response.content:


        # --------------------------
        # Claude wants to use a tool
        # --------------------------

        if block.type == "tool_use":

            print("TOOL USED:", block.name)


            if block.name == "generate_pdf":

                print("Generating PDF...")


                pdf_file = generate_pdf(
                    block.input["title"],
                    block.input["content"]
                )


                print("PDF CREATED:", pdf_file)


                assistant_response = (
                    f"I created your theater guide PDF for "
                    f"{block.input['title']}.\n\n"
                    f"File: {pdf_file}"
                )


        # --------------------------
        # Claude normal response
        # --------------------------

        elif block.type == "text":

            assistant_response += block.text



    # Save Damian response to memory
    if assistant_response:

        messages.append(
            {
                "role": "assistant",
                "content": assistant_response
            }
        )


    return assistant_response

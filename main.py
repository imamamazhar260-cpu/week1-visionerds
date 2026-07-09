from dotenv import load_dotenv
import os
from openai import OpenAI
from config import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

print("Hello user, how may I help you?")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = client.chat.completions.create(
            model="gpt-5.4",
            max_tokens=200,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        print("Bob:", response.choices[0].message.content)

    except Exception as e:

        print("\nUnable to contact OpenRouter.")
        print("Possible reasons:")
        print("- Internet is disconnected")
        print("- Invalid API Key")
        print("- Wrong model name")
        print("- API server unavailable")
        print("\nTechnical Error:")
        print(e)
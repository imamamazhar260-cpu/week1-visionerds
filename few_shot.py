from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_OPENROUTER_API_KEY"
)

response = client.chat.completions.create(
    model="openai/gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": "Clean messy sentences."
        },

        {
            "role": "user",
            "content": "i luv pyhton"
        },
        {
            "role": "assistant",
            "content": "I love Python."
        },

        {
            "role": "user",
            "content": "he dont no coding"
        },
        {
            "role": "assistant",
            "content": "He doesn't know coding."
        },

        {
            "role": "user",
            "content": "she is lernng pythn"
        }
    ]
)

print(response.choices[0].message.content)
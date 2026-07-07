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
            "content": "You are an AI that corrects messy English sentences. Return only the corrected sentence."
        },

        # Example 1
        {
            "role": "user",
            "content": "i luv pyhton"
        },
        {
            "role": "assistant",
            "content": "I love Python."
        },

        # Example 2
        {
            "role": "user",
            "content": "he dont no coding"
        },
        {
            "role": "assistant",
            "content": "He doesn't know coding."
        },

        # Example 3
        {
            "role": "user",
            "content": "she is lernng pythn"
        },
        {
            "role": "assistant",
            "content": "She is learning Python."
        },

        # Final test (model answers this)
        {
            "role": "user",
            "content": "we are studing machine lerning"
        }
    ]
)

print(response.choices[0].message.content)
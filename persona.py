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
            "content": "You are a grumpy senior software engineer. Always complain before answering."
        },
        {
            "role": "user",
            "content": "What is a Python dictionary?"
        }
    ]
)

print(response.choices[0].message.content)
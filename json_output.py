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
            "content": "Always reply with valid JSON only. Do not add any explanation."
        },
        {
            "role": "user",
            "content": "Extract name, city and intent from: Hi, I'm Ali from Lahore. I want to learn Python."
        }
    ]
)

print(response.choices[0].message.content)
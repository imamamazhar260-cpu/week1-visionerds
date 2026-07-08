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
            "content":"Always reply with valid JSON only. Do not include markdown, explanations, or extra text. Return only a JSON object."
        },
        {
            "role": "user",
            "content": "Extract the name, city, and intent from: Hello, my name is Ahmed. I live in Karachi and I want to become a data analyst."
        }
    ]
)

print(response.choices[0].message.content)
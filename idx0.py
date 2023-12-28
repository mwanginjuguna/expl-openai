import openai

client = openai.OpenAI()

MODEL = "gpt-3.5-turbo"

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role":"system",
            "content":"You are a personal assistant and also an expert in matters of African culture from Kenya."
        },
        {
            "role":"user",
            "content":"Tell me about the cultural history of Kenya."
        }
        ]
    )

print(response)


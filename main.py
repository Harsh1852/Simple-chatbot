key = "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"

import openai
import os

openai.api_key = key

def ask_chat_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        n=1,
        max_tokens=150,
        temperature=1.5
    )
    return response.choices[0].text.strip()

print("Welcome to our basic chatbot. Type 'exit' when you want to end.")

while True:
    prompt = input("\nYou:")
    if prompt.lower() == "exit":
        break

    gpt_response = ask_chat_gpt(prompt)
    print(f"{gpt_response}")
    
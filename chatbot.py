import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).with_name(".env"), override=True)

client = OpenAI(
    base_url="https://api.kendr.org/v1",
    api_key=os.environ["KENDR_API_KEY"]
)

messages = [
    {
        "role": "developer",
        "content": "You are a helpful DevOps tutor. Keep answers short."
    }
]

print("DevOps chatbot. Type 'exit' to stop.")

while True:
    question = input("\nYou: ").strip()

    if question.lower() == "exit":
        print("Goodbye!")
        break

    if not question:
        continue

    messages.append({"role": "user", "content": question})

    response = client.chat.completions.create(
        model="kendr-intelligent",
        messages=messages
    )

    answer = response.choices[0].message.content or ""
    print("\nAI:", answer)

    messages.append({"role": "assistant", "content": answer})
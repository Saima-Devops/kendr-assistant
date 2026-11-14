import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).with_name(".env"), override=True)

client = OpenAI(
    base_url="https://api.kendr.org/v1",
    api_key=os.environ["KENDR_API_KEY"]
)

question = input("What would you like to learn? ").strip()

if not question:
    print("Please enter a question.")
else:
    response = client.chat.completions.create(
        model="kendr-intelligent",
        messages=[
            {
                "role": "developer",
                "content": (
                    "You are a patient DevOps teacher. "
                    "Use simple English and include one practical example."
                )
            },
            {"role": "user", "content": question}
        ]
    )

    print("\nAnswer:")
    print(response.choices[0].message.content)
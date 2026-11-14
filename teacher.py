import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).with_name(".env"), override=True)

client = OpenAI(
    base_url="https://api.kendr.org/v1",
    api_key=os.environ["KENDR_API_KEY"]
)

response = client.chat.completions.create(
    model="kendr-intelligent",
    messages=[
        {"role": "user", "content": "Explain DevOps in two sentences."}
    ]
)

print(response.choices[0].message.content)
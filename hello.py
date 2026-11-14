import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://api.kendr.org/v1",
    api_key=os.environ["KENDR_API_KEY"]
)

completion = client.chat.completions.create(

  model="kendr-intelligent",

  messages=[

    {"role": "developer", "content": "You are a helpful assistant."},

    {"role": "user", "content": "Hello!"}

  ]

)

print(completion.choices[0].message)
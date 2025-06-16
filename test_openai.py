import os
import openai
from openai.error import OpenAIError

openai.api_key = os.getenv("OPENAI_API_KEY")  # or put your key here as a string

if not openai.api_key:
    print("API key not found. Please set the OPENAI_API_KEY environment variable.")
    exit(1)

try:
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello in a friendly way."}
        ],
        max_tokens=10
    )
    print("API call succeeded! Here's the response:")
    print(response.choices[0].message.content.strip())
except OpenAIError as e:
    print("API call failed:")
    print(e)

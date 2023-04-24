import os
import openai
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
openai.api_key = os.environ.get("OPENAI_API_KEY")

prompt = input("Ask a question: ")

response=openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.5,
    max_tokens=60,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

from io import StringIO
print(response.choices[0].text)
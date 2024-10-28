from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv("/home/da-015/Desktop/projects/sales_agent_bot/sale_agent_bot_code_base/variables/.env")

# Access the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=openai_api_key)


# Function to get response from OpenAI's API
def get_openai_response(prompt, model="gpt-4o-mini"):

    completion = client.chat.completions.create(
      model=model,
      messages= prompt
    )

    return completion.choices[0].message.content
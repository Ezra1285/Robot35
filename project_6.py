# import openai
import os
from openai import OpenAI
client = OpenAI()
os.environ["OPENAI_API_KEY"] = ""

# Define a function to interact with ChatGPT
def chat_with_gpt(prompt, voice='surprise_me'):
    
    # Send the prompt to ChatGPT and get the response
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"{question} respond like a {voice}"}
    ],
    max_tokens=10
)
    
    return response

# Example usage:
question = "What is the meaning of life?"
chosen_voice = 'pirate'  # Change the voice as desired
response = chat_with_gpt(question, voice=chosen_voice)
print(response)
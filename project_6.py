# import openai
import os
from openai import OpenAI

client = OpenAI()
os.environ["OPENAI_API_KEY"] = "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"

# Define a function to interact with ChatGPT
def chat_with_gpt(prompt, voice='surprise_me'):
    
    # Send the prompt to ChatGPT and get the response
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"{question} respond like a {voice} and give a short answer."}
    ],
    max_tokens=10
    )
    
    return response

# Example usage:
if __name__ == "__main__":
    question = "What is the meaning of life?"
    chosen_voice = 'pirate'  # Change the voice as desired
    response = chat_with_gpt(question, voice=chosen_voice)
    print(response)
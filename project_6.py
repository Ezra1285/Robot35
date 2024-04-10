import openai
import pyttsx3
import os
from openai import OpenAI

# Define a function to interact with ChatGPT
def chat_with_gpt(prompt, client, voice='surprise_me'):
    # Send the prompt to ChatGPT and get the response
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"{prompt} respond like a {voice} in a short answer."}
    ],
    max_tokens=25
    )
    # content = response.choices[0].message["content"]
    content = response.choices[3]
    return content

def speak(speech):
        engine = pyttsx3.init() 
        if (speech != " "):
        # while(speech != " "):    
            engine.say(speech)
            engine.runAndWait()

# Example usage:
if __name__ == "__main__":
    print("KEy is:", os.environ.get("OPENAI_API_KEY"))
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    # openai.my_api_key = 'YOUR_API_KEY'
    # OpenAI.api_key = os.getenv('OPENAI_API_KEY')
    # client.my_api_key = "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"
    while True:
        print("Enter your question or quit to exit:")
        question = input()
        if question == 'quit' or question == 'q':
            break
        print("Select an option:\na: pirate voice\nb: southern accent\nc: British accent")
        voice_choice = input()
        response = chat_with_gpt(question, client, voice=voice_choice)
        # response = chat_with_gpt_new(question, voice_choice)
        print(response)
        speak(response)    

    
    
    # question = "What is the meaning of life?"
    # chosen_voice = 'pirate'  # Change the voice as desired
    
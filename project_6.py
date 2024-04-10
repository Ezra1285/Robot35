# import openai
import pyttsx3
import os
import openai


# Define a function to interact with ChatGPT
def chat_with_gpt(prompt, client, voice='surprise_me'):
    
    # Send the prompt to ChatGPT and get the response
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"{prompt} respond like a {voice} and give a short answer."}
    ],
    max_tokens=10
    )
    
    return response

def speak(speech):
        engine = pyttsx3.init() 
        if (speech != " "):
        # while(speech != " "):    
            engine.say(speech)
            engine.runAndWait()

# Example usage:
if __name__ == "__main__":
    openai.my_api_key = "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"
    client = openai.OpenAI("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")
    question = "What is the meaning of life?"
    chosen_voice = 'pirate'  # Change the voice as desired
    response = chat_with_gpt(question, client, voice=chosen_voice)
    print(response)
    speak(response)
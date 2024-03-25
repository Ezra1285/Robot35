import pyttsx3

class Text_To_Speech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150) # speech rate

    def speak(self):
        if (speech != ''):
            while(True):    
                self.engine.say(speech)
                self.engine.runAndWait()
                speech = ''

def main():
    global speech
    tts = Text_To_Speech
    speech = "Hello World"
    tts.speak()

if __name__ == '__main__':
    main()
    

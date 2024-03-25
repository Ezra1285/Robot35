import pyttsx3


global speech
class Text_To_Speech:
    global speech
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
    speech = "Hello World"
    tts = Text_To_Speech
    tts.speak(tts)

if __name__ == '__main__':
    main()
    

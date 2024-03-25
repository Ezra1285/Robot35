import pyttsx3



global speech # speech is a global so it can be set anywhere we want the robot to say something
# class Text_To_Speech:
    # global speech 
    # def __init__(self):
    #     self.engine = pyttsx3.init()
    #     self.engine.setProperty('rate', 150) # speech rate

# def speak(self):
def speak():
        global speech
        engine = pyttsx3.init() 
        # if (speech != " "):
        while(speech != " "):    
            engine.say(speech)
            engine.runAndWait()
            speech = " "

def main():
    global speech
    speech = "Hello World"
    # tts = Text_To_Speech
    # tts.speak(tts)
    speak()

if __name__ == '__main__':
    main()
    

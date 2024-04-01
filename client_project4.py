import socket
import sys
import time
import pyttsx3

HOST = socket.gethostname()

SCRIPT = [
            "Hi, you look familiar.", 
            "I am from Montana, where are you from?",
            "Me too, I am from the room we are in currently in Bozeman, Montana.",
            "Tango",
            " What are the odds. Two robots run into to each other from the same state, and the same town, and the same room, with the same name?",
            "EOF"
        ]
 
def main(PORT):
    print("CLIENT host:", HOST, "\n")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            s.sendall(b"your turn")
            time.sleep(1)
            data = s.recv(1024)
            token = data.decode()
            client_line = SCRIPT.pop(0)
            if client_line == "EOF" or client_line == "done":
                break
            if not token: 
                continue
            speak(client_line)
            print("Client:", client_line)  
            time.sleep(3)
            
def speak(speech):
        engine = pyttsx3.init() 
        if (speech != " "):
        # while(speech != " "):    
            engine.say(speech)
            engine.runAndWait()

if __name__ == "__main__":
    main(int(sys.argv[1]))
import socket
import sys
import time

HOST = socket.gethostname()
PORT = 8899

SCRIPT = [
            "Hi", 
            "I was just going to say the same thing about you. Where are you from?",
            "Me too. Bozeman, Montana",
            "Me too, wow that is wild. What is your name?",
            "Your not going to believe this,  but my name is Tango also.",
            "Looking around this room I'd say pretty high.",
            "EOF"
        ]

def main(PORT):
    print("Server host:", HOST)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        
        conn, addr = s.accept()
        time.sleep(2)
        with conn:
            print(f"Connected by {addr}\n")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                if data.decode() == 'your turn':
                    server_line = SCRIPT.pop(0)
                    if server_line == 'EOF':
                        conn.sendall(b"done")        
                        break
                    time.sleep(2)
                    print("Server:", server_line)
                conn.sendall(data)
                time.sleep(1)

# TODO: Make then head slowly look left and then slkowly look right
def panHead():
    pass

if __name__ == "__main__":
    if len(sys.argv[1]) >= 3:
        port = int(sys.argv[1])
    else:
        port = PORT
    main(port)
    panHead()

import pyttsx3
import socket

host="127.0.0.1"
port=12345
ttsenggine=pyttsx3.init()
ttsenggine.setProperty('rate', 130)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    con,addr = s.accept()
    with con:
        print("Connected By", addr)
        while True:
            data = con.recv(1024)
            ttsenggine.say(data)
            if not data:
                ttsenggine.say("goodbye")
                break

            ttsenggine.runAndWait()
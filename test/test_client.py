import socket
import speech_recognition as sr
import subprocess
import threading

host="127.0.0.1"
port=12345
recogniser = sr.Recognizer()
mic = sr.Microphone()
wtospeak = threading.Event()
wtospeak.clear()
wtopush = threading.Event()
wtopush.clear()
stop = threading.Event()
stop.clear()

def push():
    stop_push = False
    while not stop_push:
        wtopush.clear()
        input()
        wtospeak.set()
        subprocess.call("pacmd set-source-mute 1 0", shell=True)
        subprocess.call("pacmd set-source-volume 1 40000", shell=True)
        input()
        subprocess.call("pacmd set-source-mute 1 1", shell=True)
        wtopush.wait()
        stop_push  =  stop.is_set()


def speak():
    flag = True
    with socket.socket() as s:
        s.connect((host, port))
        while flag:
            wtospeak.wait()
            print("speak something")
            try:
                with mic as source:
                    audio = recogniser.listen(source)
                print('done listening')
                audio_to_text = recogniser.recognize_google(audio)
                s.send(str(audio_to_text).encode('utf-8'))
            except sr.UnknownValueError:
                s.send("please try again".encode('utf-8'))
            flag = False if input("again(Y/N)")=='N' else True
            if not flag:
                stop.set()
            wtospeak.clear()
            wtopush.set()


t = threading.Thread(target=push)
q = threading.Thread(target=speak)
q.start()
t.start()

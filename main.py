import os
import eel
import threading
from engine.features import playAssistantSound

eel.init("www")

def play_sound():
    playAssistantSound()

sound_thread = threading.Thread(target=play_sound)
sound_thread.start()

os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start("index.html", mode=None, host="localhost", block=True)

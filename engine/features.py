from playsound import playsound
import eel

#playing assistanyt sound function
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\magical-sparkle-whoosh-298750.mp3"
    playsound(music_dir)
@eel.expose
def playAssistantSound2():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
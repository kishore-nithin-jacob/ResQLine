import threading
from pyaudio_prod import rec_sec
from time import sleep
from test2 import get_emotion_from_audio


print("recording audio.......")
i=1
rec_sec("audios/aud"+str(i)+".wav")
#sleep(11)
get_emotion_from_audio("audios/aud"+str(i)+".wav")
#!/bin/python3
from signal import pause
import os

from picamera2 import Picamera2
from time import sleep
import cv2

camera = Picamera2()
camera.start()

detector = cv2.QRCodeDetector()

play_command = "mpc add" 

song_names = {
        1: "Thingy",
        2: "El_Cuarto_De_Tula.mp3",
        3: "Thriller",
        4: "Oblivion.mp3",
        5: "Strangelove.mp3",
        6: "Lionel_Richie"
}

currently_playing = 0
step_duration = 0.25
seconds_to_pause = 0
data = None

while True:
    sleep(step_duration)
    try:
        img = camera.capture_array()
        data, bbox, _ = detector.detectAndDecode(img)
    except:
        pass
    print(seconds_to_pause)
    if data:
        data = int(data)
        if data == currently_playing:
            seconds_to_pause = 1
            os.system("mpc play")
        else:
            currently_playing = data
            os.system("mpc clear && mpc add \"%s\" && mpc play" % song_names[data])
    else:
        if seconds_to_pause <= 0:
            os.system("mpc pause")
        else:
            seconds_to_pause -= step_duration

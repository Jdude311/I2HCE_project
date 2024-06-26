#!/bin/python3
from gpiozero import Button
from signal import pause
import os

bounce_time_param = 0.05

play_command = "mpc add" 

song_names = {
        1: "Dancing_on_the_Ceiling",
        2: "Neil_Diamond",
        3: "Thriller",
        4: "70s_Classics && mpc shuffle",
        5: "80s_Hits && mpc shuffle",
        6: "Lionel_Richie"
}

class AlbumButton:
    number_buttons = 0
    active_button = None
    def __init__(self, pin):
        AlbumButton.number_buttons += 1
        self.number = AlbumButton.number_buttons
        self.pin = pin
        self.button = Button(pin, bounce_time=bounce_time_param)
        self.button.when_released = self.callback

    def callback(self):
        print("Button %d pressed!" % self.pin)
        song_name = song_names[self.number]
        if AlbumButton.active_button == self.number:
            os.system("mpc toggle")
        else:
            os.system("mpc clear && mpc add %s && mpc play" % song_name)
        AlbumButton.active_button = self.number

class MediaButton:
    def __init__(self, pin, media_function):
        self.pin = pin
        self.button = Button(pin, bounce_time=bounce_time_param)
        self.media_function = media_function
        self.button.when_released = self.callback

    def callback(self):
        os.system(self.media_function)

# Refresh database
os.system("mpc update") 

play_button = MediaButton(2, "mpc toggle")
album_button_pins = [3, 4, 17, 27, 22, 10]
album_buttons = []
for pin in album_button_pins:
    album_buttons.append(AlbumButton(pin))

pause()


"""
import lgpio as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
button_pins = [7, 8, 10, 37]
for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def button_callback(channel):
    print("Button was pushed!")

GPIO.add_event_detect(37, GPIO.RISING, callback=button_callback)

message = input("Enter to quite \n\n")

GPIO.cleanup()

for pin in button_pins:
    GPIO.add_event_detect(pin, GPIO.RISING, callback=button_callback)

"""

"""
while True:
    for pin in button_pins:
        if GPIO.input(pin) == GPIO.HIGH:
            print("Button " + str(pin) + " was pushed!")

"""

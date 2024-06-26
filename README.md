# Setup
Clone this repository to the home directory of the user: ```git clone https://github.com/Jdude311/I2HCE_project/edit/main/README.md```

This has two versions, one for each prototype. One is hte ```buttons.py``` file, and the other is the ```qrcode_mpd_test.py``` file. 

## Hardware
This is all running on a raspberry pi 4B.
### QR Code
Uses a raspberry pi v1.3 camera but would probably work just fine with any other camera. It's the one that uses the ribbon cable. 

### Buttons
Literally just uses buttons hooked up to GPIO pins. dead simple. You have to configure which GPIO pins have buttons on them in the ```buttons.py``` file because a proper configuration file for better configurability was out of the scope of this course, but it's really quite simple and this project has so little code that it's perfectly fine.

## Raspberry Pi Configuration
We used a Raspberry Pi 4B here with raspbian something headless. 

Default user is ```user``` with no password and autologin configured through ```raspi-config```. User must have group 29 (audio) privilege.

The actual python program is launched on startup by addling the correct launch script (either ```~/I2HCE_project/start_qrcode.sh``` or ```python ~/I2HCE_project/buttons.py```) to the end of ```.profile```. This just runs the script any time the raspberry pi turns on and logs in user. This might be better to do with a cron job but whatever.

## Required packages
unfortunately, we needed to have a mix of packages from apt and from pip. 
Apt requirements:
- mpd
- python3-picamera2
- pip
- mpc

GPIOZERO library should be preinstalled on raspberry pi os.

Python requires a venv setup in this directory to run ```qrode_mpd_test.py```.
- set up venv with root directory in ```~/I2HCE_project/```
- ```pip install -r requirements.txt```
- that's all for that

## Music for mpd
Music is stored in the ```~/Music/``` directory. This is where MPD's database is. The music should be in mp3 format.

Playlists are created by placing files in subfolders of the music directory, and are played with the command ```mpc add``` followed by the name of the folder.

Playlists play by default in alphabetical order. Name the files "1-Song_Title_Here.mp3"

Youtube playlists can be downloaded using ```yt-dlp``` using the following command: ```yt-dlp -x --audio-format mp3 -o "%(playlist_index)d-%(title)s" "https://youtube.com/playlist?list=KJSDJKFHKLSJHDLFKJHSDLKFHJSDKHF"```

The following youtube playlists were used for mixes:
- [70s_Classics](https://www.youtube.com/watch?v=5oWyMakvQew&list=PLjl8I_uytVg9Nxkhc-LxcKEWPDy-hn2pA)
- [80s_Hits](https://www.youtube.com/watch?v=djV11Xbc914&list=PLGBuKfnErZlDYOaD2bOazzCYvy13ozt7C)

## MPD configuration
You msut run ```ln -s ~/I2HCE_project/mpd.conf ~/.config/mpd/``` in order to configure MPD correctly.

MPD is run as a systemctl user service. Run ```systemctl --user enabe mpd.service``` to set this up.


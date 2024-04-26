# Setup
## Required packages
unfortunately, we needed to have a mix of packages from apt and from pip. 
Apt requirements:
- mpd
- python3-picamera2
- pip
- mpc

Python requires a venv setup in this directory to run the qrcode one.
- set up venv
- ```pip install -r requirements.txt```
- that's all for that

## Music for mpd
Music is stored in the ```~/Music/``` directory. This is where MPD's database is. The music should be in mp3 format.

Playlists are created by placing files in subfolders of the music directory, and are played with the command ```mpc add``` followed by the name of the folder.

Playlists play by default in alphabetical order. Name the files "1-Song_Title_Here.mp3"

Youtube playlists can be downloaded using ```yt-dlp``` using the following command: ```yt-dlp -x --audio-format mp3 -o "%(playlist_index)d-%(title)s" "https://youtube.com/playlist?list=KJSDJKFHKLSJHDLFKJHSDLKFHJSDKHF"```

## MPD configuration
You msut run ```ln -s ~/I2HCE_project/mpd.conf ~/.config/mpd/``` in order to configure MPD correctly.

MPD is run as a systemctl user service. Run ```systemctl --user enabe mpd.service``` to set this up.

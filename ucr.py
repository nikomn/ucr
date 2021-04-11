from mutagen.wave import WAVE
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
import os
import random
import sys, select

def create_filler(filler_file, seconds):
    os.system("sox " + filler_file + " filler-trimmed.wav trim 0 0:" + seconds + ".000 fade 0 -0 5 > /dev/null 2>&1")

def play_with_vlc(file):
    os.system("vlc -I dummy " + file + " --play-and-exit > /dev/null 2>&1")

def read_playlist(playlist_file):
    with open(playlist_file) as f:
        content = f.read().splitlines()
    
    return random.choice(content)
    
    

def get_lenght(audio_file):
    audio_length = -1
    if audio_file.lower().endswith("mp3"):
        audio = MP3(audio_file)
        audio_length = audio.info.length
    if audio_file.lower().endswith("flac"):
        audio = FLAC(audio_file)
        audio_length = audio.info.length
    if audio_file.lower().endswith("wav"):
        audio = WAVE(audio_file)
        audio_length = audio.info.length
    return int(round(audio_length))

def get_artist_title_album(audio_file):
    # Can have different form...
    # 1:
    # ARTIST=...
    # TITLE=...
    # ALBUM=...
    # 2:
    # TIT2=...
    # TPE1=...
    # TALB=...
    # ...


    artist = "unknown artist"
    title = "unknown song"
    album = "unknown album"
    
    # If filepath has spaces it must be enclosed in quotes to play in vlc
    # ...but with mutagen it should not be in quotes, so lets remove quotes...
    if audio_file.lower().endswith('"') and audio_file.lower().startswith('"'):
        audio_file = audio_file[1:-1]
    try:
        if audio_file.lower().endswith("mp3"):
            audio = MP3(audio_file)
            try:
                title = audio["TIT2"]
            except:
                title = audio["TITLE"]
            try:
                artist = audio["TPE1"]
            except:
                artist = audio["ARTIST"]
            try:
                album = audio["TALB"]
            except:
                album = audio["ALBUM"]
        if audio_file.lower().endswith("flac"):
            audio = FLAC(audio_file)
            try:
                title = audio["TIT2"]
            except:
                title = audio["TITLE"]
            try:
                artist = audio["TPE1"]
            except:
                artist = audio["ARTIST"]
            try:
                album = audio["TALB"]
            except:
                album = audio["ALBUM"]
        if audio_file.lower().endswith("wav"):
            audio = WAVE(audio_file)
            try:
                title = audio["TIT2"]
            except:
                title = audio["TITLE"]
            try:
                artist = audio["TPE1"]
            except:
                artist = audio["ARTIST"]
            try:
                album = audio["TALB"]
            except:
                album = audio["ALBUM"]
    except:
        print("Error while reading file metadata!")
    
    return [artist, title, album]




# print("This is Underground Campus Radio!")
os.system("cat logo.txt")

# Custom playlist for testing...
playlist = "example.playlist"
if len(sys.argv) == 2 and sys.argv[1].endswith(".playlist"):
    print("Setting playlist to " + sys.argv[1] + " (hope you know what you are doing...)")
    playlist = sys.argv[1]


radio_on = True

while radio_on:
    test = random.randint(0,19)

    if test == 4:
        filler_length = random.randint(15,45)
        print("Next program starting soon...")
        create_filler("filler.wav", str(filler_length))
        play_with_vlc("filler-trimmed.wav")
    
    # example.playlist is assuming that the listed files will be at
    # current users Music directory
    # Playlist creation
    # find ~/Music -type f > example.playlist + some editing...

    song = '"/home/' + os.getlogin() + read_playlist(playlist) + '"'
    artist_title = get_artist_title_album(song)
    print("Now playing:", artist_title[0], "-", artist_title[1], "- from the album", artist_title[2])
    play_with_vlc(song)
    print("To stop playing press any key")
    inputs, outputs, errors = select.select( [sys.stdin], [], [], 2 )
    for keypress in inputs:
        if keypress == sys.stdin:
            input_data = sys.stdin.readline()
            # print("enteri found!")
            radio_on = False
    print()


# print(read_playlist("example.playlist"))

print("This is Underground Campus Radio - program ending for the day, see you later!")

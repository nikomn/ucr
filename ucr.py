from mutagen.wave import WAVE
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
import os

def create_filler(filler_file, seconds):
    os.system("sox " + filler_file + " filler-trimmed.wav trim 0 0:" + seconds + ".000 fade 0 -0 5 > /dev/null 2>&1")

def play_with_vlc(file):
    os.system("vlc -I dummy " + file + " --play-and-exit > /dev/null 2>&1")

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



print("This is Underground Campus Radio!")

print("Next program staring soon...")
create_filler("filler.wav", "25")
play_with_vlc("filler-trimmed.wav")

print("Now playing: Dead Kennedys - Hyperactive Child... (" + str(get_lenght("song1.mp3")) + " seconds)")
play_with_vlc("song1.mp3")

print("Next program staring soon...")
create_filler("filler.wav", "15")
play_with_vlc("filler-trimmed.wav")

print("Now playing: The Who - Armenia City in the Sky... (" + str(get_lenght("song2.mp3")) + " seconds)")
play_with_vlc("song2.mp3")

print("Now playing: The Yardbirds - Train Kept Rollin' (live)... (" + str(get_lenght("song3.flac")) + " seconds)")
play_with_vlc("song3.flac")

print("Next program staring soon...")
create_filler("filler.wav", "40")
play_with_vlc("filler-trimmed.wav")

print("Now playing: Pop Profile - John Lennon... (" + str(get_lenght("program.mp3")) + " seconds)")
play_with_vlc("program.mp3")

print("This is Underground Campus Radio - program ending for the day, see you later!")

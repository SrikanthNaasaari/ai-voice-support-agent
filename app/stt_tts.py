# Folder: app/stt_tts.py
import speech_recognition as sr
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import os

def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=5)
    with open("audio/temp_input.wav", "wb") as f:
        f.write(audio.get_wav_data())
    return "audio/temp_input.wav"

def speech_to_text(audio_path):
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)
    return r.recognize_google(audio)

def text_to_speech(text):
    engine = pyttsx3.init()
    temp_wav = "audio/temp_response.wav"
    engine.save_to_file(text, temp_wav)
    engine.runAndWait()
    return temp_wav


# def text_to_speech(text, chunk_size=200):
#     engine = pyttsx3.init()
#     temp_wav = "audio/temp_response.wav"
#     engine.setProperty('rate', 170)  # Optional: Adjust speed
#     engine.setProperty('volume', 1)  # Optional: Set volume level (0 to 1)
    
#     # Break the response into smaller chunks if it's too long
#     chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    
#     # Ensure the engine processes each chunk completely
#     for chunk in chunks:
#         # Save each chunk to a temporary WAV file
#         engine.save_to_file(chunk, temp_wav)
#         engine.runAndWait()  # Wait for speech to finish before continuing
    
#     return temp_wav


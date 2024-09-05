import pyttsx3
from colorama import Fore, Style
import threading

class SpeechGenerator:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        
        # Set default properties
        self.engine.setProperty('rate', 150)    # Speed of speech
        self.engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
        
        # Set default voice (usually index 0 is the default system voice)
        self.set_voice(0)

        self.lock = threading.Lock()

    def set_voice(self, index):
        if 0 <= index < len(self.voices):
            self.engine.setProperty('voice', self.voices[index].id)
            print(f"Voice set to: {self.voices[index].name}")
        else:
            print(f"Invalid voice index. Please choose between 0 and {len(self.voices) - 1}")

    def list_available_voices(self):
        print("Available voices:")
        for i, voice in enumerate(self.voices):
            print(f"{i}: {voice.name} ({voice.id})")

    def set_rate(self, rate):
        self.engine.setProperty('rate', rate)
        print(f"Speech rate set to: {rate}")

    def set_volume(self, volume):
        if 0.0 <= volume <= 1.0:
            self.engine.setProperty('volume', volume)
            print(f"Volume set to: {volume}")
        else:
            print("Volume must be between 0.0 and 1.0")

    def text_to_speech(self, text):
        with self.lock:
            self.engine.say(text)
            self.engine.runAndWait()

# Create a global instance of SpeechGenerator
speech_generator = SpeechGenerator()

def speak(text, color=Fore.CYAN):
    print(f"{color}Astacus >: {text}{Style.RESET_ALL}")
    speech_generator.text_to_speech(text)

def set_voice(index):
    speech_generator.set_voice(index)

def list_voices():
    speech_generator.list_available_voices()

def set_speech_rate(rate):
    speech_generator.set_rate(rate)

def set_speech_volume(volume):
    speech_generator.set_volume(volume)
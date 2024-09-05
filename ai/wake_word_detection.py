import speech_recognition as sr
import time

class WakeWordDetector:
    def __init__(self, wake_word="hey ace", timeout=5):
        self.wake_word = wake_word.lower()
        self.timeout = timeout
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening for wake word...")
            try:
                audio = self.recognizer.listen(source, timeout=self.timeout)
                text = self.recognizer.recognize_google(audio).lower()
                print(f"Heard: {text}")
                return self.wake_word in text
            except sr.WaitTimeoutError:
                return False
            except sr.UnknownValueError:
                print("Could not understand audio")
                return False
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return False

    def start_listening(self):
        while True:
            if self.listen():
                print("Wake word detected!")
                return True
            time.sleep(0.1)  # Short pause to prevent excessive CPU usage
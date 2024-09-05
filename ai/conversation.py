import speech_recognition as sr
from ai.llm_interface import get_chatgpt_message
from ai.speech_generation import speak

WAKE_WORD = "hey ace"

class Conversation:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mode = 'text'

    def listen(self, timeout=None, phrase_time_limit=None):
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text.lower()
            except sr.WaitTimeoutError:
                return None
            except sr.UnknownValueError:
                print("Sorry, I didn't understand that.")
                return None
            except sr.RequestError:
                print("Sorry, there was an error with the speech recognition service.")
                return None

    def get_response(self, user_input):
        context = f"The user said: '{user_input}'. Provide a short, relevant response as Astacus."
        return get_chatgpt_message(context)

    def text_interaction(self):
        user_input = input("You: ")
        if user_input.lower() == 'switch to voice':
            speak("Switching to voice mode. Say 'switch to text' to return to text mode.")
            self.mode = 'voice'
            return True
        elif user_input.lower() in ['exit', 'quit', 'bye']:
            speak("Goodbye!")
            return False
        response = self.get_response(user_input)
        speak(response)
        return True

    def voice_interaction(self):
        user_input = self.listen(timeout=5, phrase_time_limit=5)
        if user_input:
            if user_input == 'switch to text':
                speak("Switching to text mode. Type 'switch to voice' to return to voice mode.")
                self.mode = 'text'
            elif user_input in ['exit', 'quit', 'bye']:
                speak("Goodbye!")
                return False
            else:
                response = self.get_response(user_input)
                speak(response)
        return True

    def run(self):
        speak(f"We're starting in {self.mode} mode. You can switch modes at any time.")
        
        while True:
            if self.mode == 'text':
                if not self.text_interaction():
                    break
            else:  # voice mode
                wake_word_detected = False
                while not wake_word_detected:
                    print("Listening for wake word...")
                    audio = self.listen(timeout=None, phrase_time_limit=3)
                    if audio and WAKE_WORD in audio:
                        wake_word_detected = True
                        speak("Yes, I'm here. What can I do for you?")
                
                if not self.voice_interaction():
                    break

def start_conversation(mode='text'):
    conversation = Conversation()
    conversation.mode = mode
    conversation.run()
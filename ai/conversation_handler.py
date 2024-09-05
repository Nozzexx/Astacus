import sys
import time
from ai.speech_generation import speak
from ai.llm_interface import get_chatgpt_message

class ConversationHandler:
    def __init__(self, timeout=60):
        self.timeout = timeout

    def process_input(self, user_input):
        if user_input.lower() in ['exit', 'quit', 'bye']:
            return "Goodbye!"
        else:
            response = self.get_response(user_input)
            return response

    def get_response(self, user_input):
        context = f"The user said: '{user_input}'. Provide a short, relevant response as Astacus."
        return get_chatgpt_message(context)
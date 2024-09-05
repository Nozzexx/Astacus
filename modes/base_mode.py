from abc import ABC, abstractmethod
from ai.speech_generation import speak

class BaseMode(ABC):
    @abstractmethod
    def enter(self):
        """Method called when entering the mode"""
        pass

    @abstractmethod
    def exit(self):
        """Method called when exiting the mode"""
        pass

    @abstractmethod
    def run(self):
        """Main loop of the mode"""
        pass

    @abstractmethod
    def handle_input(self, input_data):
        """Handle user input specific to this mode"""
        pass

    def display_instructions(self):
        """Display instructions for the current mode"""
        speak(f"Instructions for {self.__class__.__name__}:")
        speak("Use 'help' to see these instructions again.")
        speak("Use 'switch mode' to change to a different mode.")
        speak("Use 'exit' to end the conversation.")
        # Add any mode-specific instructions here
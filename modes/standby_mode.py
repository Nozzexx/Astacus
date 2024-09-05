from modes.base_mode import BaseMode
from colorama import Fore, Style
from ai.speech_generation import speak

class StandbyMode(BaseMode):
    def enter(self):
        speak("Entering Standby Mode.")

    def exit(self):
        speak("Exiting Standby Mode.")

    def run(self):
        # This method is required by the BaseMode abstract class
        # In standby mode, we don't need to do anything in the run loop
        # as we're just waiting for input, which is handled by handle_input
        pass

    def handle_input(self, input_data):
        if input_data.lower() == "help":
            self.display_instructions()
            return None
        elif input_data.lower() == "switch mode":
            return "switch_mode"
        elif input_data.lower() == "exit":
            return "shutdown"
        else:
            print(Fore.YELLOW + f"Astacus >: Standby Mode received command: {input_data}" + Style.RESET_ALL)
            return None

    def display_instructions(self):
        super().display_instructions()
        speak("In Standby Mode, I'm waiting for your commands.")
        speak("You can ask me to switch to a different mode or give me a task.")
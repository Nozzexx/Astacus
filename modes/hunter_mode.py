from modes.base_mode import BaseMode
from ai.speech_generation import speak
from utils.logger import logger
import time

class HunterMode(BaseMode):
    def __init__(self):
        super().__init__()
        self.target = None
        self.is_hunting = False

    def enter(self):
        speak("Entering Hunter Mode. Ready to track targets.")
        logger.info("Hunter Mode activated")

    def exit(self):
        speak("Exiting Hunter Mode.")
        self.stop_hunting()
        logger.info("Hunter Mode deactivated")

    def handle_input(self, user_input):
        user_input = user_input.lower()

        if "set target" in user_input:
            self.set_target(user_input.split("set target")[1].strip())
        elif "start hunting" in user_input:
            self.start_hunting()
        elif "stop hunting" in user_input:
            self.stop_hunting()
        elif "status" in user_input:
            self.report_status()
        else:
            return self.general_conversation(user_input)

    def run(self):
        """Continuous operation method for Hunter Mode"""
        while self.is_hunting:
            # Simulate hunting behavior
            logger.info(f"Searching for target: {self.target}")
            time.sleep(5)  # Wait for 5 seconds between "searches"
            # In a real implementation, this would involve sensor data processing,
            # movement control, etc.

    def set_target(self, target):
        self.target = target
        speak(f"Target set to: {self.target}")
        logger.info(f"Hunter Mode: Target set to {self.target}")

    def start_hunting(self):
        if not self.target:
            speak("No target set. Please set a target before starting the hunt.")
        else:
            self.is_hunting = True
            speak(f"Starting to hunt for {self.target}")
            logger.info(f"Hunter Mode: Started hunting for {self.target}")
            # In a real implementation, you might start a new thread here to run the 'run' method

    def stop_hunting(self):
        if self.is_hunting:
            self.is_hunting = False
            speak("Stopped hunting.")
            logger.info("Hunter Mode: Stopped hunting")
        else:
            speak("Not currently hunting.")

    def report_status(self):
        if self.target:
            status = f"Current target: {self.target}. "
            status += "Actively hunting." if self.is_hunting else "Not currently hunting."
        else:
            status = "No target set. Not currently hunting."
        speak(status)

    def general_conversation(self, user_input):
        # Handle general conversation or queries related to Hunter mode
        if "what is hunter mode" in user_input:
            return "Hunter mode allows me to track and locate specific targets in the environment."
        elif "how does hunting work" in user_input:
            return "In Hunter mode, I use my sensors to scan the area for the specified target, analyzing visual and audio cues to locate it."
        else:
            return f"I'm in Hunter mode, focused on tracking targets. Your input: '{user_input}' doesn't seem to be a Hunter mode command. Can you clarify or ask something related to hunting or tracking?"

    def display_instructions(self):
        instructions = [
            "Hunter Mode Instructions:",
            "1. 'Set target [name]' - Set a specific target to hunt",
            "2. 'Start hunting' - Begin the hunting process",
            "3. 'Stop hunting' - Cease all hunting activities",
            "4. 'Status' - Report current hunting status",
            "You can also ask general questions about Hunter mode or how hunting works."
        ]
        for instruction in instructions:
            speak(instruction)
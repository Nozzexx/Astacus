from modes.base_mode import BaseMode

class StealthMode(BaseMode):
    def enter(self):
        print("Entering Stealth Mode")

    def exit(self):
        print("Exiting Stealth Mode")

    def run(self):
        print("Running Stealth Mode")
        # Add your mode-specific logic here

    def handle_input(self, input_data):
        print(f"Handling input in Stealth Mode: {input_data}")
        # Add input handling specific to this mode
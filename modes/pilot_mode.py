from modes.base_mode import BaseMode

class PilotMode(BaseMode):
    def enter(self):
        print("Entering Pilot Mode")

    def exit(self):
        print("Exiting Pilot Mode")

    def run(self):
        print("Running Pilot Mode")
        # Add your mode-specific logic here

    def handle_input(self, input_data):
        print(f"Handling input in Pilot Mode: {input_data}")
        # Add input handling specific to this mode
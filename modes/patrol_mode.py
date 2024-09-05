from modes.base_mode import BaseMode

class PatrolMode(BaseMode):
    def enter(self):
        print("Entering Patrol Mode")

    def exit(self):
        print("Exiting Patrol Mode")

    def run(self):
        print("Running Patrol Mode")
        # Add your mode-specific logic here

    def handle_input(self, input_data):
        print(f"Handling input in Patrol Mode: {input_data}")
        # Add input handling specific to this mode
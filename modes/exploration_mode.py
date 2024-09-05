from modes.base_mode import BaseMode

class ExplorationMode(BaseMode):
    def enter(self):
        print("Entering Exploration Mode")

    def exit(self):
        print("Exiting Exploration Mode")

    def run(self):
        print("Running Exploration Mode")
        # Add your mode-specific logic here

    def handle_input(self, input_data):
        print(f"Handling input in Exploration Mode: {input_data}")
        # Add input handling specific to this mode
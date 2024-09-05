from modes.base_mode import BaseMode

class RelaxedMode(BaseMode):
    def enter(self):
        print("Entering Relaxed Mode")

    def exit(self):
        print("Exiting Relaxed Mode")

    def run(self):
        print("Running Relaxed Mode")
        # Add your mode-specific logic here

    def handle_input(self, input_data):
        print(f"Handling input in Relaxed Mode: {input_data}")
        # Add input handling specific to this mode
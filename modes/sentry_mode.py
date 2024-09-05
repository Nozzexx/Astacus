from modes.base_mode import BaseMode

class SentryMode(BaseMode):
    def enter(self):
        print("Entering Sentry Mode")

    def exit(self):
        print("Exiting Sentry Mode")

    def run(self):
        print("Running Sentry Mode")
        # Add your mode-specific logic here

    def handle_input(self, input_data):
        print(f"Handling input in Sentry Mode: {input_data}")
        # Add input handling specific to this mode
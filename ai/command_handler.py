from ai.speech_generation import speak

class CommandHandler:
    def __init__(self, astacus):
        self.astacus = astacus

    def handle_command(self, command):
        command_parts = command.lower().split()
        if not command_parts:
            speak("I'm sorry, I didn't catch that command. Could you please repeat?")
            return

        main_command = command_parts[0]

        if main_command == "help":
            self.display_help()
        elif main_command == "list" and len(command_parts) > 1 and command_parts[1] == "modes":
            self.list_modes()
        elif main_command == "set" and len(command_parts) > 1 and command_parts[1] == "mode":
            if len(command_parts) > 2:
                self.set_mode(" ".join(command_parts[2:]))
            else:
                speak("Please specify a mode to set.")
        else:
            speak(f"I'm sorry, I don't recognize the command '{command}'. Say 'Ace help' for a list of available commands.")

    def display_help(self):
        speak("Here are the available commands:")
        speak("'Ace help' - Display this help message")
        speak("'Ace list modes' - List all available modes")
        speak("'Ace set mode [mode name]' - Switch to a specific mode")

    def list_modes(self):
        modes = self.astacus.mode_controller.get_available_modes()
        speak("Available modes are:")
        for mode in modes:
            speak(mode)

    def set_mode(self, mode_name):
        if self.astacus.set_mode(mode_name):
            speak(f"Switched to {mode_name} mode.")
        else:
            speak(f"Failed to switch to {mode_name} mode. Please check if it's a valid mode.")
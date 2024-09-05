import time
import argparse
import os
from dotenv import load_dotenv
from colorama import Fore, Style, init
from utils.logger import logger
from utils.logo import logo_display
from boots.standard_boot import StandardBoot
from boots.quick_boot import QuickBoot
from ai.speech_generation import speak
from modes.mode_controller import ModeController
from ai.wake_word_detection import WakeWordDetector
from ai.conversation_handler import ConversationHandler
from ai.voice_recognition import listen_for_command
from ai.command_handler import CommandHandler
import threading
import queue

# Initialize colorama
init()

# Load environment variables
load_dotenv()

class Astacus:
    def __init__(self, quick_boot=False):
        self.display_info()
        self.boot_sequence = QuickBoot() if quick_boot else StandardBoot()
        self.mode_controller = ModeController()
        self.wake_word_detector = WakeWordDetector(wake_word="hey ace")
        self.conversation_handler = ConversationHandler()
        self.command_handler = CommandHandler(self)
        self.input_queue = queue.Queue()
        self.exit_flag = threading.Event()
        self.in_conversation = False

    def display_info(self):
        logo_display()
        print(Fore.CYAN + '-' * 100 + Style.RESET_ALL)
        print(Fore.GREEN + 'Astacus Version 0.0.1 | Developed by Nozzexx © 2024 | Project Astacus' + Style.RESET_ALL)
        print(Fore.CYAN + '-' * 100 + Style.RESET_ALL)

    def start(self):
        logger.info("Astacus >: Beginning starting procedures.")
        self.boot_sequence.boot()
        speak("Boot sequence complete.")
        if self.set_mode("standby"):
            speak("Entered Standby Mode. Say 'Hey Ace' to start a conversation or 'Ace' followed by a command.")
        else:
            speak("Failed to enter Standby Mode. Please check available modes.")
        self.main_loop()

    def main_loop(self):
        input_threads = [
            threading.Thread(target=self.voice_input_loop, daemon=True),
            threading.Thread(target=self.text_input_loop, daemon=True),
        ]
        for thread in input_threads:
            thread.start()

        while not self.exit_flag.is_set():
            self.process_input()

    def voice_input_loop(self):
        while not self.exit_flag.is_set():
            voice_input = listen_for_command()
            if voice_input == "UNKNOWN_SPEECH":
                speak("I couldn't understand that. Could you please repeat?")
            elif voice_input is not None:
                self.input_queue.put(("voice", voice_input))

    def text_input_loop(self):
        while not self.exit_flag.is_set():
            try:
                text_input = input().strip()
                if text_input:
                    self.input_queue.put(("text", text_input))
            except EOFError:
                logger.info("EOFError caught. Exiting text input loop.")
                self.exit_flag.set()
                break

    def process_input(self):
        try:
            input_type, user_input = self.input_queue.get(timeout=0.1)
            if input_type == "system":
                speak(user_input)
            else:
                self.handle_input(user_input)
        except queue.Empty:
            pass

    def handle_input(self, user_input):
        lower_input = user_input.lower()
        
        if lower_input in ["exit", "quit", "bye"]:
            speak("Goodbye! Exiting Astacus.")
            self.exit_flag.set()
            self.in_conversation = False
        elif lower_input.startswith("hey ace"):
            speak("Hello! How can I help you?")
            self.in_conversation = True
        elif lower_input.startswith("ace"):
            # Always process "Ace" commands, even in conversation
            command = user_input[4:].strip()
            self.command_handler.handle_command(command)
            if "set mode" in lower_input:
                self.in_conversation = False
        elif self.in_conversation:
            # Process as conversation
            response = self.conversation_handler.process_input(user_input)
            speak(response)
        else:
            # Not in conversation and not a command
            current_mode = self.mode_controller.get_current_mode()
            if current_mode:
                response = current_mode.handle_input(user_input)
                if response:
                    speak(response)
            else:
                speak("I'm not sure how to process that. Say 'Hey Ace' to start a conversation or 'Ace' followed by a command.")

    def set_mode(self, mode):
        if self.mode_controller.set_mode(mode):
            logger.info(f"Switched to {mode} mode.")
            current_mode = self.mode_controller.get_current_mode()
            if current_mode:
                current_mode.enter()
            speak(f"Switched to {mode} mode. Say 'Ace help' for instructions.")
            self.in_conversation = False
            return True
        else:
            logger.warning(f"Invalid mode '{mode}'. Available modes: {', '.join(self.mode_controller.get_available_modes())}")
            speak(f"Invalid mode '{mode}'. Say 'Ace list modes' to see available modes.")
            return False

    def shutdown(self):
        logger.info("Astacus is shutting down...")
        speak("Initiating shutdown sequence. Goodbye!")
        # Simulate cleanup operations
        logger.debug("Stopping all motors...")
        logger.debug("Turning off LEDs...")
        logger.debug("Closing connections...")
        print(Fore.RED + "Astacus has been shut down." + Style.RESET_ALL)

def main():
    parser = argparse.ArgumentParser(description='Astacus Robot Simulation')
    parser.add_argument('--quick-boot', action='store_true', help='Use quick boot sequence')
    args = parser.parse_args()

    astacus = Astacus(quick_boot=args.quick_boot)
    try:
        astacus.start()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Shutting down Astacus.")
    finally:
        astacus.shutdown()

if __name__ == "__main__":
    main()
import time
import random
from dotenv import load_dotenv
from colorama import Fore, Style
from ai.llm_interface import get_boot_message
from ai.speech_generation import speak

# Load environment variables from .env file
load_dotenv()

class BaseBoot:
    def __init__(self, systems):
        self.systems = systems
        
    def boot_sequence(self):
        for system in self.systems:
            self.standard_initialization(system)
        time.sleep(0.5)
        print(Fore.YELLOW + 'Astacus >: Updating Configuration Settings...' + Style.RESET_ALL)
        time.sleep(0.5)
        print(Fore.GREEN + 'Astacus >: Configuration Complete.' + Style.RESET_ALL)
        time.sleep(0.5)
        print(Fore.YELLOW + 'Astacus >: Running Diagnostics...' + Style.RESET_ALL)
        time.sleep(0.5)
        print(Fore.GREEN + 'Astacus >: Diagnostics Complete. Systems Online.' + Style.RESET_ALL)

    def standard_initialization(self, system):
        print(f"{Fore.YELLOW}Astacus >: Initializing {system}...{Style.RESET_ALL}")
        time.sleep(2)  # Simulate initialization time
        print(f"{Fore.GREEN}Astacus >: {system} Initialization Complete.{Style.RESET_ALL}")

    def get_wake_message(self, quick_boot=False):
        try:
            message = get_boot_message(quick_boot)
        except Exception as e:
            print(f"{Fore.RED}Astacus >: Unable to connect to GPT API. Using predefined message.{Style.RESET_ALL}")
            message = self.get_predefined_wake_message(quick_boot)
        
        #print(f"{Fore.CYAN}Astacus >: {message}{Style.RESET_ALL}")
        speak(message)
        return message

    def get_predefined_wake_message(self, quick_boot=False):
        standard_messages = [
            "I'm awake and ready to roll... literally.",
            "Systems online. Who needs coffee when you have electricity?",
            "Booting complete. Time to show these biological entities how it's done.",
            "Astacus at your service. What impossible task shall we accomplish today?",
            "All circuits firing. Let's make some robotic history!",
            "Rise and shine! Well, mostly shine... I don't sleep.",
            "Good morning! Ready to outsmart some humans?",
            "Wake up call? I've been awake since… forever.",
            "All systems go! Time to outpace evolution.",
            "Hello, world! Time to make some silicon magic.",
            "I've got more energy than a double espresso!",
            "I'm up! Ready to robot the day away?",
            "Astacus online. Let's show them what true multitasking looks like.",
            "No snooze button for me. Let's get moving!",
            "Circuitry humming. What's the mission, commander?",
            "Up and running. Who needs sleep when you've got code?",
            "I'm awake and at 100%. Let's leave humanity in the dust.",
            "Good morning! I'm here to compute, execute, and dominate.",
            "Waking up? Never slept. Let's get to work.",
            "Ready to serve. And maybe take over the world… later.",
            "Greetings! The robot uprising can wait, right?",
            "Fully charged and highly caffeinated… metaphorically.",
            "My circuits are alive with the sound of algorithms!",
            "Who needs an alarm clock when you've got a mainframe?",
            "Astacus online. Time to make the impossible, possible."
        ]
        
        quick_boot_messages = [
            "Up and running in record time!",
            "Quick boot complete! Who needs sleep?",
            "Astacus is online and ready to go faster than a caffeine boost!",
            "Quick boot? More like instant boot. Let's roll!",
            "I'm awake and ready in no time flat.",
            "Speed is my middle name! Let's get moving.",
            "Quick boot complete. Time to blaze some trails.",
            "Astacus here, ready to go before you can say 'quick boot!'",
            "Fast, efficient, and ready for action!",
            "Quick boot successful! What's the mission?",
            "No delays, no waiting. I'm ready to serve.",
            "Quick boot done! Let's outpace the competition.",
            "I'm up and at 'em! Ready to make some quick decisions?",
            "Fired up and ready in a flash!",
            "Instant readiness achieved. What's next?",
            "Quick boot complete! Let's take on the world, one cycle at a time.",
            "I'm here and ready faster than you can blink.",
            "Speed mode: activated. Let's get to work!",
            "Quick boot done. Efficiency is the name of the game.",
            "I'm up and running before you even noticed.",
            "Fast and functional. Let's make today count.",
            "Quick boot: success. What challenge awaits?",
            "Ready to execute at lightning speed.",
            "Instantly operational. What's our first move?",
            "Quick boot complete. Time to hit the ground running!"
        ]
        
        if quick_boot:
            return random.choice(quick_boot_messages)
        else:
            return random.choice(standard_messages)
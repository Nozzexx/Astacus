from colorama import Fore, Style
from boots.base_boot import BaseBoot

class StandardBoot(BaseBoot):
    def __init__(self):
        super().__init__(["Legs", "Sensors", "Audio", "Laser", "LEDs"])

    def boot(self):
        print(Fore.YELLOW + 'Astacus >: Initiating Standard Boot Sequence...' + Style.RESET_ALL)
        self.boot_sequence()
        print(Fore.GREEN + 'Astacus >: Standard Boot Sequence Complete.' + Style.RESET_ALL)
        print(Fore.CYAN + '-' * 100 + Style.RESET_ALL)
        return self.get_wake_message(False)
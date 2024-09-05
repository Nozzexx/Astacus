from colorama import Fore, Style
from boots.base_boot import BaseBoot

class QuickBoot(BaseBoot):
    def __init__(self):
        super().__init__(["Legs", "Sensors"])

    def boot(self):
        print(Fore.YELLOW + 'Astacus >: Initiating Quick Boot Sequence...' + Style.RESET_ALL)
        self.boot_sequence()
        print(Fore.GREEN + 'Astacus >: Quick Boot Sequence Complete.' + Style.RESET_ALL)
        print(Fore.CYAN + '-' * 100 + Style.RESET_ALL)
        return self.get_wake_message(True)
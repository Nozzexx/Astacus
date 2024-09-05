from modes.standby_mode import StandbyMode
from modes.exploration_mode import ExplorationMode
from modes.hunter_mode import HunterMode
from modes.patrol_mode import PatrolMode
from modes.pilot_mode import PilotMode
from modes.sentry_mode import SentryMode
from modes.stealth_mode import StealthMode
from modes.relaxed_mode import RelaxedMode
# Import other mode classes as needed

class ModeController:
    def __init__(self):
        self.modes = {
            "standby": StandbyMode(),
            "exploration": ExplorationMode(),
            "patrol": PatrolMode(),
            "pilot": PilotMode(),
            "hunter": HunterMode(),
            "relaxed": RelaxedMode(),
            "sentry": SentryMode(),
            "stealth": StealthMode(),
            # Add other modes here, e.g.:
            # "exploration": ExplorationMode(),
            # "patrol": PatrolMode(),
        }
        self.current_mode = None

    def set_mode(self, mode_name):
            if mode_name.lower() in self.modes:
                if self.current_mode:
                    self.current_mode.exit()
                self.current_mode = self.modes[mode_name.lower()]
                return True
            return False

    def get_current_mode(self):
            return self.current_mode

    def get_available_modes(self):
            return list(self.modes.keys())
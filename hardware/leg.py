from utils.logger import logger

class LegController:
    def __init__(self):
        self.legs = ['FR', 'MR', 'BR', 'FL', 'ML', 'BL']
        logger.info("LegController initialized")

    def move_leg(self, leg_id, angle):
        if leg_id in self.legs:
            logger.debug(f"Moving leg {leg_id} to angle {angle}")
        else:
            logger.warning(f"Invalid leg ID: {leg_id}")

    def move_all_legs(self, angles):
        if len(angles) == len(self.legs):
            for leg, angle in zip(self.legs, angles):
                self.move_leg(leg, angle)
        else:
            logger.warning("Invalid number of angles provided")

    def reset_position(self):
        logger.info("Resetting all legs to default position")
        self.move_all_legs([0, 0, 0, 0, 0, 0])
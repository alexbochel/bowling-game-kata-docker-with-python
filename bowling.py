
class BowlingGame:
    def __init__(self):
        self.score = 0

    def roll(self, pins_knocked_over):
        self.score += pins_knocked_over
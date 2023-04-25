import random
from constants import WIDTH, HEIGHT, BARRIER_HEIGHT, TICK_LENGTH

BARRIER_VELOCITY = -70


class BarrierModel:

    def __init__(self):
        self.reset()

    def tick(self):
        self.x = self.x + BARRIER_VELOCITY*TICK_LENGTH
        if self.x < 0:
            self.reset()

    def reset(self):
        self.y = random.randint(0, HEIGHT - BARRIER_HEIGHT)
        self.x = WIDTH

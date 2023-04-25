from constants import HEIGHT, BARRIER_HEIGHT, TICK_LENGTH, BIRD_X
import math

ACCELERATION = 350
JUMP_VELOCITY = -200


class BirdModel:

    def __init__(self):
        self.y = HEIGHT/2
        self.v = 0

    def outside_range(self):
        return self.y < 0 or self.y > HEIGHT

    def hit_barrier(self, barrier):
        return BIRD_X == math.floor(barrier.x) and (self.y < barrier.y or self.y > barrier.y + BARRIER_HEIGHT)

    def tick(self):
        self.v = self.v + ACCELERATION*TICK_LENGTH
        self.y = self.y + self.v*TICK_LENGTH

    def jump(self):
        self.v = JUMP_VELOCITY

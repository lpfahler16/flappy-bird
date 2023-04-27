from BirdModel import BirdModel
from BarrierModel import BarrierModel
from constants import HEIGHT, BIRD_X, BARRIER_HEIGHT


class FlappyBirdModel:

    def __init__(self):
        self.score = 0
        self.bird = BirdModel()
        self.barrier = BarrierModel()
        self.barrier.register(self)

    def game_state(self):
        return {
            'birdY': self.bird.y,
            'birdV': self.bird.v,
            'score': round(self.score, 3),
            'barrierX': self.barrier.x,
            'barrierY': self.barrier.y
        }

    def game_state_evolve(self):
        return [
            self.bird.y,  # Distance to top
            HEIGHT - self.bird.y,  # Distance to bottom
            self.barrier.x - BIRD_X,  # Distance to barrier
            self.bird.y - self.barrier.y,  # Distance to top of barrier
            # Distance to bottom of barrier
            self.bird.y - (self.barrier.y + BARRIER_HEIGHT),
            self.bird.v  # Bird velocity
        ]

    def tick(self):
        self.bird.tick()
        self.barrier.tick()
        self.score += 0.0001

    def jump(self):
        self.bird.jump()

    def notify(self):
        self.score += 1

    def game_over(self):
        return self.bird.outside_range() or self.bird.hit_barrier(self.barrier)

from BirdModel import BirdModel
from BarrierModel import BarrierModel


class FlappyBirdModel:

    def __init__(self):
        self.score = 0
        self.bird = BirdModel()
        self.barrier = BarrierModel()

    def game_state(self):
        return {
            'birdY': self.bird.y,
            'birdV': self.bird.v,
            'score': self.score,
            'barrierX': self.barrier.x,
            'barrierY': self.barrier.y
        }

    def tick(self):
        self.bird.tick()
        self.barrier.tick()
        self.score += 1

    def jump(self):
        self.bird.jump()

    def game_over(self):
        return self.bird.outside_range() or self.bird.hit_barrier(self.barrier)

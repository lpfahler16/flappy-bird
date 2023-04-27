from joblib import load
from constants import HEIGHT, BIRD_X, BARRIER_HEIGHT


class EvolvePlayer:

    def __init__(self):
        self.player = load('best_evolved_play.joblib')

    def jump(self, game_state):
        result = self.player.process([
            game_state['birdY'],  # Distance to top
            HEIGHT - game_state['birdY'],  # Distance to bottom
            game_state['barrierX'] - BIRD_X,  # Distance to barrier
            # Distance to top of barrier
            game_state['birdY'] - game_state['barrierY'],
            # Distance to bottom of barrier
            game_state['birdY'] - (game_state['barrierY'] + BARRIER_HEIGHT),
            game_state['birdV']  # Bird velocity
        ])
        return result[0] > result[1]

from collections import defaultdict
from enum import Enum
import json
from FlappyBirdModel import FlappyBirdModel


class Action(Enum):
    FLAP = 1
    FALL = 0


UP = Action.FLAP
DOWN = Action.FALL


class QController:
    # State is represented as a 4-element tuple (birdY, birdV, barrierX, barrierY)

    def __init__(self, model: FlappyBirdModel):
        self.alpha = 0.7
        self.rewards = {0: 0, 1: -1000}
        # The key cannot is the state tuple described above and the move (flap or no flap): ((state), move)
        self.Q = defaultdict((lambda: 0))
        self.model = model
        self.update_state()

    @staticmethod
    def state_to_dict(state):
        '''
        Converts the tuple representation of state from the q learning algorithm
        to a dictionary used by the model'''
        s = {}
        s["birdY"], s["birdV"], s["barrierX"], s["barrierY"] = state
        return s

    @staticmethod
    def state_to_tuple(state):
        '''
        Converts the dictionary representation of state from the model
        to a tuple that can be used as keys for the q table'''
        return (state["birdY"], state["birdV"], state["barrierX"], state["barrierY"])

    def update_state(self):
        self.state = self.model.game_state()
        # remove the score used by the model, does not distinguish state in training
        self.state.pop("score")
        return self.state

    def best_action(self, state):
        '''Expects state in tuple form'''
        return UP if self.Q[(state, UP)] > self.Q[(state, DOWN)] else DOWN  # Observe the default is to fall (both will be 0)

    def move(self, action):
        '''TODO 3:
        Figure out tick behavior: should only behave every ten ticks?'''
        if action == UP:
            self.model.flap()
        self.model.tick()
        self.update_state()

    def Pi(self, state, epsilon):
        '''TODO 2:
        Need to discourage flapping when too high and falling when too low.
        Can be done with simple 
        `if state[0] > <CLOSE_TO_TOP> return DOWN else if state[0] < <CLOSE_TO_BOTTOM> return UP`'''
        best = self.best_action(state)

        random = random.choice(list(Action))

        return random.choice([random, best], p=[epsilon, 1-epsilon])

    def save_q(self):
        print(f"Saving q table - {len(self.Q.items())} elements")
        with open("q_values.json", "w") as f:
            json.dump(self.Q, f)

    def run_experiment(self, epsilon=0.25, lam=0.95, num_trials=10000):
        for trial in range(num_trials):
            while not self.model.game_over():
                s = QController.state_to_tuple(self.state)
                # Determine the best action according to the q table
                # a = self.best_action(QController.state_to_tuple(self.state))
                a = self.Pi(s, epsilon)

                self.move(a)

                s1 = QController.state_to_tuple(self.state)

                s1_reward = self.rewards[1] if self.model.game_over(
                ) else self.rewards[0]

                self.Q[(s, a)] = s1_reward + self.Q[(s1, self.best_action(s1))]

                epsilon *= lam

                s = s1

        self.save_q()

        time_survived = 0

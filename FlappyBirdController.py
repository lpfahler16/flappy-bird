import time
import pygame
from constants import TICK_LENGTH


class FlappyBirdController:

    def __init__(self, model, view, player):
        self.model = model
        self.view = view
        self.player = player

    def play(self):
        pygame.init()
        last_tick = time.time()
        running = True
        while running:
            seconds = time.time() - last_tick

            if (seconds > TICK_LENGTH):
                self.model.tick()
                self.view.draw(self.model.game_state())
                last_tick = time.time()

                if self.player.jump(self.model.game_state()):
                    self.model.jump()

                if (self.model.game_over()):
                    pygame.quit()

        pygame.quit()

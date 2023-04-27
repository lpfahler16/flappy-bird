import pygame


class HumanPlayer:

    def __init__(self):
        pass

    def jump(self, game_state):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return True

        return False

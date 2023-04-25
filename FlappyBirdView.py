import pygame
from constants import WIDTH, HEIGHT, BIRD_X, BARRIER_HEIGHT


class FlappyBirdView:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Flappy Bird")

        self.bg_color = (255, 255, 255)
        self.screen.fill(self.bg_color)
        self.rect_color = (255, 0, 0)
        pygame.display.flip()

    def draw(self, game_state):
        self.screen.fill(self.bg_color)
        bird = pygame.Rect(BIRD_X, game_state['birdY'], 20, 20)
        pygame.draw.rect(self.screen, self.rect_color, bird)

        barrier_top = pygame.Rect(
            game_state['barrierX'], 0, 20, game_state['barrierY'])
        pygame.draw.rect(self.screen, self.rect_color, barrier_top)

        barrier_bottom = pygame.Rect(
            game_state['barrierX'], game_state['barrierY'] + BARRIER_HEIGHT, 20, HEIGHT)
        pygame.draw.rect(self.screen, self.rect_color, barrier_bottom)

        pygame.display.set_caption(
            f"Flappy Bird -- score: {game_state['score']}")
        pygame.display.flip()

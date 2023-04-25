import time
import pygame
from constants import TICK_LENGTH
from FlappyBirdModel import FlappyBirdModel
from FlappyBirdView import FlappyBirdView


model = FlappyBirdModel()
pygame.init()
view = FlappyBirdView()

last_tick = time.time()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            model.jump()
    seconds = time.time() - last_tick

    if (seconds > TICK_LENGTH):
        model.tick()
        view.draw(model.game_state())
        last_tick = time.time()

        if (model.game_over()):
            pygame.quit()

pygame.quit()

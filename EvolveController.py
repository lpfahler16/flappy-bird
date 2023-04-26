import time
import pygame
from constants import TICK_LENGTH
from FlappyBirdModel import FlappyBirdModel
from FlappyBirdView import FlappyBirdView
from joblib import load


model = FlappyBirdModel()
pygame.init()
view = FlappyBirdView()
player = load('best_evolved_play.joblib')

last_tick = time.time()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    seconds = time.time() - last_tick

    if (seconds > TICK_LENGTH):
        model.tick()
        view.draw(model.game_state())
        last_tick = time.time()

        state = model.game_state()
        result = player.process([state['birdY'], state['barrierX'],
                                state['barrierY'], state['birdV']])

        if result[0] > result[1]:
            model.jump()

        if (model.game_over()):
            pygame.quit()

pygame.quit()

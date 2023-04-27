import time
import pygame
from constants import TICK_LENGTH
from FlappyBirdModel import FlappyBirdModel
from FlappyBirdView import FlappyBirdView
from FlappyBirdController import FlappyBirdController
from EvolvePlayer import EvolvePlayer
from joblib import load

model = FlappyBirdModel()
view = FlappyBirdView()
player = EvolvePlayer()
controller = FlappyBirdController(model, view, player)
controller.play()

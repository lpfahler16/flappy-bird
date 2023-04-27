import time
import pygame
from constants import TICK_LENGTH
from FlappyBirdModel import FlappyBirdModel
from FlappyBirdView import FlappyBirdView
from HumanPlayer import HumanPlayer
from FlappyBirdController import FlappyBirdController


model = FlappyBirdModel()
view = FlappyBirdView()
player = HumanPlayer()
controller = FlappyBirdController(model, view, player)
controller.play()

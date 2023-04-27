from FlappyBirdModel import FlappyBirdModel
from FlappyBirdView import FlappyBirdView
from FlappyBirdController import FlappyBirdController
from EvolvePlayer import EvolvePlayer

model = FlappyBirdModel()
view = FlappyBirdView()
player = EvolvePlayer()
controller = FlappyBirdController(model, view, player)
controller.play()

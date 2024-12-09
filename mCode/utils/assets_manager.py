import random

import pygame


# store all images here

class AssetsManager:
    def __init__(self):
        self.assets = {
            'button': pygame.image.load("../graphics/other/btn.png").convert_alpha(),
            'clickButton': pygame.image.load("../graphics/other/clickBtn.png").convert_alpha(),
        }

    def getRandomCar(self):
        ran = random.randint(1,6)
        return assetsManager.get("car" + str(ran))

    def get(self, key):
        return self.assets[key]


assetsManager = AssetsManager()

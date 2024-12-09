import pygame
from pygame import Vector2

from mCode.sceens.Game import Game
from mCode.utils.Button import Button
from mCode.utils.util import utils


class MainMenu(Game):
    def __init__(self):
        self.buttons = []

        self.buttons.append(Button(1, Vector2(550, 100), "Level 1",Vector2(3,2)))
        self.buttons.append(Button(2, Vector2(550, 200), "Level 2", Vector2(3, 2)))
        self.buttons.append(Button(3, Vector2(550, 300), "Level 3", Vector2(3, 2)))

        self.buttons.append(Button(4, Vector2(550, 500), "High Scores", Vector2(3, 2)))
        self.buttons.append(Button(5, Vector2(550, 600), "Quit", Vector2(3, 2)))


    def update(self):
        pass

    def draw(self):
        for button in self.buttons:
            button.draw()

    def onKeyDown(self, key):
        pass

    def onKeyUp(self, key):
        pass

    def onMouseDown(self, event):
        for button in self.buttons:
            button.onMouseDown()
            if button.clicked:
                if button.id == 1:
                    from mCode.sceens.Level1 import Level1
                    utils.currentScreen = Level1()
                    break
                if button.id == 2:
                    from mCode.sceens.Level2 import Level2
                    utils.currentScreen = Level2()
                    break
                if button.id == 3:
                    from mCode.sceens.Level3 import Level3
                    utils.currentScreen = Level3()
                    break
                if button.id == 4:
                    from mCode.sceens.HighScores import HighScores
                    utils.currentScreen = HighScores()
                    break
                if button.id == 5:
                    exit(1)

    def onMouseUp(self, event):
        for button in self.buttons:
            button.onMouseUp()



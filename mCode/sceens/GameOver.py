import pygame
from pygame import Vector2

from mCode.sceens.Game import Game
from mCode.utils.Button import Button
from mCode.utils.util import utils


class GameOver(Game):
    def __init__(self,score=0):
        self.score = score

        self.buttons = []
        self.buttons.append(Button(4, Vector2(550, 500), "Menu", Vector2(3, 2)))
        self.buttons.append(Button(5, Vector2(550, 600), "Quit", Vector2(3, 2)))

        utils.saveScore(self.score)

    def update(self):
        pass

    def draw(self):
        text = "Game Over!"
        tw = utils.font32.render(text,True,(0,0,0)).get_width()
        utils.drawText(Vector2(utils.width/2 - tw/2,100),text,(255,255,255),utils.font32)

        text = "Your score: " + str(self.score)
        tw = utils.font32.render(text, True, (0, 0, 0)).get_width()
        utils.drawText(Vector2(utils.width / 2 - tw / 2, 200), text, (255, 255, 255), utils.font32)

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
                    break
                if button.id == 3:
                    break
                if button.id == 4:
                    from mCode.sceens.MainMenu import MainMenu
                    utils.currentScreen = MainMenu()
                    break
                if button.id == 5:
                    exit(1)

    def onMouseUp(self, event):
        for button in self.buttons:
            button.onMouseUp()



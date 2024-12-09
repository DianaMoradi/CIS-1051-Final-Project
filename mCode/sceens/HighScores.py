import pygame
from pygame import Vector2

from mCode.sceens.Game import Game
from mCode.utils.Button import Button
from mCode.utils.util import utils


class HighScores(Game):
    def __init__(self):
        self.buttons = []
        self.buttons.append(Button(3, Vector2(utils.width-200, utils.height - 80), "Back", Vector2(3, 2)))
        self.scores = utils.loadScores()
        self.scores = self.scores[0:10]


    def update(self):
        pass

    def draw(self):
        for button in self.buttons:
            button.draw()
        utils.drawText(Vector2(140, 40), "Top 10 high scores: ", (23, 233, 233), utils.font32)

        self.scores = self.scores[0:10]
        y = 100
        x = 250
        i = 1
        for score in self.scores:
            pygame.draw.rect(utils.screen, (233, 233, 233), (x - 200, y - 10, 450, 50), 2)
            pygame.draw.rect(utils.screen, (233, 233, 233), (x - 200, y - 10, 100, 50), 2)

            utils.drawText(Vector2(x - 150, y), str(i), (233, 233, 233), utils.font24)
            utils.drawText(Vector2(x, y), f"{score}", (233, 123, 233), utils.font24)
            y += 48
            i += 1

    def onKeyDown(self, key):
        pass

    def onKeyUp(self, key):
        pass

    def onMouseDown(self, event):
        for button in self.buttons:
            button.onMouseDown()
            if button.clicked:
                if button.id == 3:
                    from mCode.sceens.MainMenu import MainMenu
                    utils.currentScreen = MainMenu()

    def onMouseUp(self, event):
        for button in self.buttons:
            button.onMouseUp()



#Title: Beakout Game
#Name: Diana Moradi
#Date: 12/09/2024


import pygame
from mCode.utils.util import utils

from mCode.sceens.MainMenu import MainMenu

utils.currentScreen = MainMenu()

while True:
    utils.screen.fill((23, 23, 23), (0, 0, utils.width, utils.height))
    utils.initDeltaTime()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN:
            utils.currentScreen.onKeyDown(event.key)
        if event.type == pygame.KEYUP:
            utils.currentScreen.onKeyUp(event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
            utils.currentScreen.onMouseDown(event)
            mousex, mousey = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            utils.currentScreen.onMouseUp(event)
        if event.type == pygame.MOUSEWHEEL:
            utils.currentScreen.onMouseWheel(event)

    utils.currentScreen.update()
    utils.currentScreen.draw()

    # utils.showFps()

    pygame.display.flip()



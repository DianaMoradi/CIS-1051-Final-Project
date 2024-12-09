
import pygame
import math
from pygame.locals import *

from pygame import Vector2, mixer, time

# a global class
# store global variable, functions

class Utils():

    def __init__(self):

        pygame.init()

        self.width = 1280
        self.height = 720

        self.screen = pygame.display.set_mode((self.width, self.height), DOUBLEBUF, 16)
        self.dt = 0
        self.clock = pygame.time.Clock()

        self.currentScreen = None

        self.font18 = pygame.font.Font('../graphics/other/Unicorn.ttf', 18)
        self.font24 = pygame.font.Font('../graphics/other/Unicorn.ttf', 24)
        self.font32 = pygame.font.Font('../graphics/other/Unicorn.ttf', 32)


    def initDeltaTime(self):  # calculate deltaTime
        t = self.clock.tick(60)
        self.dt = t / 1000

    def deltaTime(self):
        return self.dt

    def drawText(self, pos, text, color, font):  # draw text
        text = font.render(text, True, color)
        self.screen.blit(text, (pos.x, pos.y))

    def distance(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)

    def rotate(self, surface, angle, pivot, offset):
        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)
        rotated_offset = offset.rotate(angle)
        rect = rotated_image.get_rect(center=pivot + rotated_offset)
        return rotated_image, rect

    def saveScore(self,score):
        f = open("scores.txt", "a")
        f.write(str(score) + "\n")
        print("save")
        f.close()

    def loadScores(self):
        scores = []
        try:
            with open('scores.txt') as f:
                lines = f.readlines()
                for line in lines:
                    scores.append(int(line))
                f.close()
            scores.sort(reverse=True)
        except:
            print("error")
        return scores

    def getPath(self,file):
        # Open the file in read mode
        with open(file, "r") as f:
            # Read all lines from the file
            lines = f.readlines()
        coordinates = []

        # Process each line
        for line in lines:
            # Strip any trailing whitespace characters like \n
            line = line.strip()
            # Split the line by the comma to get mouseX and mouseY
            mouseX, mouseY = line.split(',')
            mouseX = int(mouseX)
            mouseY = int(mouseY)
            # Append the coordinates as a tuple to the list
            coordinates.append(Vector2(mouseX, mouseY))

        # Now coordinates list contains all the (mouseX, mouseY) tuples
        return coordinates


utils = Utils()  # util is global object

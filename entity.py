import sys
import pygame

class entity(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 76
        self.char = pygame.image.load('media/standing.png')

    def draw(self,win):
        win.blit(self.char, (self.x, self.y))

    def relocate(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

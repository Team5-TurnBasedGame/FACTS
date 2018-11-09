import sys
import pygame

class entity(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 12
        self.walkCount = 0
        self.walkRight = [pygame.image.load('media/R1.png'), pygame.image.load('media/R2.png'), pygame.image.load('media/R3.png'), pygame.image.load('media/R4.png'), pygame.image.load('media/R5.png'), pygame.image.load('media/R6.png'), pygame.image.load('media/R7.png'), pygame.image.load('media/R8.png'), pygame.image.load('media/R9.png')]
        self.walkLeft = [pygame.image.load('media/L1.png'), pygame.image.load('media/L2.png'), pygame.image.load('media/L3.png'), pygame.image.load('media/L4.png'), pygame.image.load('media/L5.png'), pygame.image.load('media/L6.png'), pygame.image.load('media/L7.png'), pygame.image.load('media/L8.png'), pygame.image.load('media/L9.png')]
        self.char = pygame.image.load('media/standing.png')

    def draw(self,win):
        win.blit(self.char, (self.x, self.y))

    def relocate(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

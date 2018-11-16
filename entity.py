import sys
import pygame

class entity():
    def __init__(self, x, y, width, height, char, unit = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 12 #number of pixels the image must move before the next frame of animation plays
        self.char = char
        self.unit = unit

    def draw(self,win):
        win.blit(self.char, (self.x, self.y))

    def relocate(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

class unit():
    def __init__(self, walkRight, walkLeft, hp=10, spd=5, atk=3, ranged = None):
        self.hp = hp
        self.spd = spd
        self.atk = atk
        self.walkRight = walkRight
        self.walkLeft = walkLeft

    def canMoveTo(self, destinationX, destinationY):
        if abs(destinationX - self.x) + abs(destinationY - self.y) > spd:
            return False
        else:
            return True
    
    def attack(self, entity):
        entity.takeDamage(self.atk)

    def takeDamage(self, damage):
        self.hp -= damage

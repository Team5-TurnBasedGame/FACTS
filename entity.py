import sys
import pygame

class entity():
    def __init__(self, game, x, y, width, height, char, unit = None):
        self.game = game
        self.x = x
        self.y = y
        self.displayX = x * 76
        self.displayY = y * 76
        self.width = width
        self.height = height
        self.vel = 12 #number of pixels the image must move before the next frame of animation plays
        self.char = char
        self.unit = unit

    def draw(self,win):
        win.blit(self.char, (self.displayX, self.displayY))

    def relocate(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

class unit():
    def __init__(self, walkRight, walkLeft, hp=10, spd=5, atk=3, ranged=None, ai=None):
        self.hp = hp
        self.spd = spd
        self.atk = atk
        self.walkRight = walkRight
        self.walkLeft = walkLeft
        self.ai = ai

    def canMoveTo(self, destinationX, destinationY):
        if abs(destinationX - self.x) + abs(destinationY - self.y) > spd:
            return False
        else:
            return True

    def move_to(self, x, y):
        distanceX = x - self.x
        distanceY = y - self.y

        if (distanceX > 0):
            for i in range(0, distanceX):
                move_right()
        if (distanceX < 0):
            for i in range(distanceX, 0):
                move_left()
        if (distanceY > 0):
            for i in range(0, distanceY):
                move_down()
        if (distanceY < 0):
            for i in range(distanceY, 0):
                move_up()
        
    def move_right(self):
        self.x -= 1
        self.game.animations.append(("right", self))
    def move_up(self):
        self.y -= 1
        self.game.animations.append(("up", self))
    def move_down(self):
        self.y += 1
        self.game.animations.append(("down", self))
    def move_left(self):
        self.x += 1
        self.game.animations.append(("left", self))
        
    def attack(self, entity):
        entity.takeDamage(self.atk)

    def takeDamage(self, damage):
        self.hp -= damage

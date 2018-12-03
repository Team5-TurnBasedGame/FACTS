import sys
import pygame

class Entity:
    def __init__(self, game, x, y, width, height, char):
        self.game = game
        self.x = x
        self.y = y
        self.displayX = x * 65
        self.displayY = y * 65
        self.width = width
        self.height = height
        self.vel = 5 #number of pixels the image must move before the next frame of animation plays
        self.char = char

    def draw(self, win):
        win.blit(self.char, (self.displayX, self.displayY))

    def relocate(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

class Unit(Entity):
    def __init__(self, game, x, y, width, height, char, standing, walkRight, walkLeft, walkUp, walkDown, attack, death, dead, hp=10, spd=5, atk=3, ai=None, team="enemy"):
        Entity.__init__(self, game, x, y, width, height, char)
        self.hp = hp
        self.spd = spd
        self.atk = atk
        self.char = char
        self.standing = standing
        self.walkRight = walkRight
        self.walkLeft = walkLeft
        self.walkUp = walkUp
        self.walkDown = walkDown
        self.attack = attack
        self.death = death
        self.dead = dead
        self.ai = ai
        self.team = team
        
        self.guide = []

    def draw(self, win):
        win.blit(self.char, (self.displayX, self.displayY))
        for tile in self.guide:
            (x,y) = tile
            x *= 65
            y *= 65
            win.blit(self.char, (x, y))

    def can_move_to(self, destinationX, destinationY):
        if abs(destinationX - self.x) + abs(destinationY - self.y) > self.spd:
            return False
        else:
            return True

    def move(self):
        self.guide.reverse()
        for tile in self.guide:
            (x,y) = tile
            self.move_to(x,y)
            self.guide = []
        self.game.next_entity()

    def move_to(self, x, y):
        distanceX = x - self.x
        distanceY = y - self.y

        if (distanceX > 0):
            for i in range(0, distanceX):
                self.move_right()
        if (distanceX < 0):
            for i in range(distanceX, 0):
                self.move_left()
        if (distanceY > 0):
            for i in range(0, distanceY):
                self.move_down()
        if (distanceY < 0):
            for i in range(distanceY, 0):
                self.move_up()
        
    def move_right(self):
        self.x += 1
        self.game.animations.append(("right", self))
    def move_up(self):
        self.y -= 1
        self.game.animations.append(("up", self))
    def move_down(self):
        self.y += 1
        self.game.animations.append(("down", self))
    def move_left(self):
        self.x -= 1
        self.game.animations.append(("left", self))

    def move_guide(self, direction):

        for item in self.guide:
            print(item)
        
        if direction == 'left':
            deltaX = -1
            deltaY = 0
        if direction == 'right':
            deltaX = 1
            deltaY = 0
        if direction == 'up':
            deltaX = 0
            deltaY = -1
        if direction == 'down':
            deltaX = 0
            deltaY = 1

        if self.guide == []:
            destinationX = self.x + deltaX
            destinationY = self.y + deltaY
        else:
            tile = self.guide.pop()
            destinationX = tile[0] + deltaX
            destinationY = tile[1] + deltaY
            
        if self.can_move_to(destinationX, destinationY):
            if self.guide == []:
                self.guide.append((destinationX, destinationY))
            else:
                if tile == (destinationX, destinationY):
                    return
                else:
                    self.guide.append(tile)
                    self.guide.append((destinationX, destinationY))
        else:
            self.guide.append(tile)
            print("Can't move here")
        
    def attack(self):
        entity.take_damage(self.atk)
        self.game.next_entity()

    def take_damage(self, damage):
        self.hp -= damage

    def die(self):
        self.animations.append(("die", self.current_entity))
        self.team = "dead"

class FighterAi():
    def __init__(self, game):
        self.game = game
        
    def take_turn(self):
        print("The entity contemplates life.")
        #self.take_damage(10)
        self.game.next_entity()

    def take_damage(self, damage):
        self.hp -= damage

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
        self.vel = 13 #number of pixels the image must move before the next frame of animation plays
        self.char = char

    def draw(self, win):
        win.blit(self.char, (self.displayX, self.displayY))

    def relocate(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

class Unit(Entity):
    
    def __init__(self, game, x, y, width, height, char, standing, walkRight, walkLeft, walkUp, walkDown, attack, death, dead, hp=10, spd=5, attackdist=1, atk=3, team="enemy"):
        Entity.__init__(self, game, x, y, width, height, char)
        self.hp = hp
        self.spd = spd
        self.attackdist = attackdist
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
        self.team = team
        
        self.guide = []
        self.attackguide = []

        self.guidechar = pygame.image.load('media/walkGuide.png')
        self.attackchar = pygame.image.load('media/attackGuide.png')

    def draw(self, win):
        win.blit(self.char, (self.displayX, self.displayY))
        for tile in self.guide:
            (x,y) = tile
            x *= 65
            y *= 65
            win.blit(self.guidechar, (x, y))
        for tile in self.attackguide:
            (x,y) = tile
            x *= 65
            y *= 65
            win.blit(self.attackchar, (x, y))

    def can_move_to(self, destinationX, destinationY):
        if abs(destinationX - self.x) + abs(destinationY - self.y) > self.spd:
            return False
        else:
            for e in self.game.entities:
                if destinationX == e.x and destinationY == e.y and e.team != self.team:
                    return False
            return True

    def move(self):
        self.guide.reverse()
        for tile in self.guide:
            (x,y) = tile
            self.move_to(x,y)
            self.guide = []
        self.game.action = 'attack'

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
            try:
                self.guide.append(tile)
            except:
                pass
            print("Can't move here")

    def can_attack(self, destinationX, destinationY):
        if (abs(destinationX - self.x) + abs(destinationY - self.y) > self.attackdist):
            return False
        else:
            return True
        
    def attack_guide(self, direction):

        for item in self.attackguide:
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

        if self.attackguide == []:
            destinationX = self.x + deltaX
            destinationY = self.y + deltaY
        else:
            tile = self.attackguide.pop()
            destinationX = tile[0] + deltaX
            destinationY = tile[1] + deltaY
            
        if self.can_attack(destinationX, destinationY):
            if self.attackguide == []:
                self.attackguide.append((destinationX, destinationY))
            else:
                if tile == (destinationX, destinationY):
                    return
                else:
                    self.attackguide.append(tile)
                    self.attackguide.append((destinationX, destinationY))
        else:
            self.attackguide.append(tile)
            print("Can't attack this spot")
        
    def deal_damage(self):
        for e in self.game.entities:
            for tile in self.attackguide:
                (x,y) = tile
                if e.x == x and e.y == y and e.team != self.team:
                    self.game.animations.append(("attack", self))
                    e.take_damage(self.atk)
        self.attackguide = []
        self.game.action = None
        self.game.next_entity()

    def take_damage(self, damage):
        self.hp -= damage
        print("The entity took damage!")
        print(self.hp)

    def die(self):
        self.game.animations.append(("die", self))
        self.team = "dead"

class FighterAi(Unit):
    def __init__(self, game, x, y, width, height, char, standing, walkRight, walkLeft, walkUp, walkDown, attack, death, dead, hp=10, spd=5, attackdist=1, atk=3, team="enemy"):
        Unit.__init__(self, game, x, y, width, height, char, standing, walkRight, walkLeft, walkUp, walkDown, attack, death, dead, hp=10, spd=5, attackdist=1, atk=3, team="enemy")
        
    def take_turn(self):
        target = Entity(None, 999, 999, None, None, None) #dummy entity, arbitrarily far away
        for e in self.game.entities:
            if self.team != e.team and e.team != 'dead':
                if self.get_distance((e.x, e.y)) < self.get_distance((target.x, target.y)):
                    target = e
        (x,y) = (target.x, target.y)
        if abs(self.x - x) > 1 or abs(self.y - y) > 1:
            self.move_towards((x,y))
        else:
            pass
        if abs(self.x - x) <= self.attackdist and abs(self.y - y) <= self.attackdist:
            print("in range of target")
            print(abs(self.x - target.x))
            print(abs(self.y - target.y))
            self.ai_deal_damage(target)
        else:
            pass
        self.game.next_entity()

    def move_towards(self, location):
        (x, y) = location
        print("The orc wants to move, but can't!")
        for s in range(self.spd):
            print("s: "+str(s))
            print("selfloc = " +str((self.x, self.y)))
            print("targetloc = " +str(location))
            if self.x > x:
                if self.can_move_to(self.x-1, self.y):
                    self.move_left()
            elif self.x < x:
                if self.can_move_to(self.x+1, self.y):
                    self.move_right()
            elif self.y < y:
                if self.can_move_to(self.x, self.y+1):
                    self.move_down()
            elif self.y > y:
                if self.can_move_to(self.x, self.y-1):
                    self.move_up()


    def get_distance(self, location):
        (x, y) = location
        return abs(x - self.x) + abs(y - self.y)

    def ai_deal_damage(self, target):
        print("The enemy delt damage!")
        target.take_damage(self.atk)
        self.game.animations.insert(0, ("attack", self))

    def take_damage(self, damage):
        self.hp -= damage

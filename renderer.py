import sys, pygame

class Renderer:
    def __init__(self, game):

        self.tilewidth, self.tileheight = game.stateinfo.get("screen")
        self.tiles = [[0] * self.tileheight for i in range(self.tilewidth)]
        self.size = self.width, self.height = self.tileheight*76, self.tilewidth*76
        self.screen = pygame.display.set_mode(self.size)
        self.square = pygame.image.load("square.png")
        self.squarerect = self.square.get_rect()
        self.man = game.entities[-1]
        
    def render(self):
        black = 0, 0, 0
        self.screen.fill(black)
        
        for i in range(self.width):
            for j in range(self.height):
                self.squarerect.top = i*76
                self.squarerect.left = j*76
                self.screen.blit(self.square, self.squarerect)
        self.man.draw(self.screen)
        pygame.display.flip()

    def walkRight(self):
        counter = 0
        n = 0
        while counter < 76:
            self.screen.blit(self.man.char, (self.man.x, self.man.y))
            self.man.x += self.man.vel
            counter += self.man.vel
            if n < 8:
                self.man.char = self.man.walkRight[n]
                n += 1
            else:
                n = 0
            self.render()
        self.man.char = pygame.image.load('media/standing.png')

    def walkLeft(self):
        counter = 0
        n = 0
        while counter < 76:
            self.screen.blit(self.man.char, (self.man.x, self.man.y))
            self.man.x -= self.man.vel
            counter += self.man.vel
            if n < 8:
                self.man.char = self.man.walkLeft[n]
                n += 1
            else:
                n = 0
            self.render()
        self.man.char = pygame.image.load('media/standing.png')

    def walkUp(self):
        counter = 0
        while counter < 76:
            self.screen.blit(self.man.char, (self.man.x, self.man.y))
            self.man.y -= self.man.vel
            counter += self.man.vel
            self.render()
        self.man.char = pygame.image.load('media/standing.png')

    def walkDown(self):
        counter = 0
        while counter < 76:
            self.screen.blit(self.man.char, (self.man.x, self.man.y))
            self.man.y += self.man.vel
            counter += self.man.vel
            self.render()
        self.man.char = pygame.image.load('media/standing.png')

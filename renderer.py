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

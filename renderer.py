import sys, pygame

class Renderer:
    def __init__(self, tilewidth, tileheight):
        self.tiles = [[0] * tileheight for i in range(tilewidth)]
        self.size = self.width, self.height = tileheight*76, tilewidth*76
        self.screen = pygame.display.set_mode(self.size)
        self.square = pygame.image.load("square.png")
        self.squarerect = self.square.get_rect()
        
        
    def render(self):
        black = 0, 0, 0
        self.screen.fill(black)
        
        for i in range(self.width):
            for j in range(self.height):
                self.squarerect.top = i*76
                self.squarerect.left = j*76
                self.screen.blit(self.square, self.squarerect)

        for i in
        pygame.display.flip()
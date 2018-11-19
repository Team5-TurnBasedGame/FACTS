import sys, pygame

class Renderer:
    def __init__(self, screen):

        self.tilewidth, self.tileheight = screen
        self.tiles = [[0] * self.tileheight for i in range(self.tilewidth)]
        self.size = self.width, self.height = self.tileheight*76, self.tilewidth*76
        self.screen = pygame.display.set_mode(self.size)
        self.square = pygame.image.load("square.png")
        self.squarerect = self.square.get_rect()
        
    def render(self):

        self.renderBackground()
        pygame.display.flip()

    def animate(self, currentAnim, currentEntity):
        if currentAnim == "right":
            self.walkRight(currentEntity)
        elif currentAnim == "left":
            self.walkLeft(currentEntity)
        elif currentAnim == "up":
            self.walkUp(currentEntity)
        elif currentAnim == "down":
            self.walkDown(currentEntity)
        pygame.display.flip()

    def renderBackground(self):
        black = 0, 0, 0
        self.screen.fill(black)

        for i in range(self.width):
            for j in range(self.height):
                self.squarerect.top = i*76
                self.squarerect.left = j*76
                self.screen.blit(self.square, self.squarerect)

    def render_entities(self, entities):
        for e in entities:
            e.draw(self.screen)

    def renderTitleScreen(self):
        blue = 0, 0, 255
        self.screen.fill(blue)

    def renderLevelSelect(self):
        green = 0, 255, 0
        self.screen.fill(green)

    def walkRight(self, entity):
        counter = 0
        n = 0
        while counter < 76:
            self.renderBackground()
            entity.displayX += entity.vel
            counter += entity.vel
            if n < 8:
                entity.char = entity.walkRight[n]
                n += 1
            else:
                n = 0
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = pygame.image.load('media/standing.png')
        

    def walkLeft(self, entity):
        counter = 0
        n = 0
        while counter < 76:
            self.renderBackground()
            entity.displayX -= entity.vel
            counter += entity.vel
            print(counter)
            if n < 8:
                entity.char = entity.walkLeft[n]
                n += 1
            else:
                n = 0
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = pygame.image.load('media/standing.png')

    def walkUp(self, entity):
        counter = 0
        while counter < 76:
            self.renderBackground()
            entity.displayY -= entity.vel
            counter += entity.vel
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = pygame.image.load('media/standing.png')

    def walkDown(self, entity):
        counter = 0
        while counter < 76:
            self.renderBackground()
            entity.displayY += entity.vel
            counter += entity.vel
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = pygame.image.load('media/standing.png')

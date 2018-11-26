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

        self.render_background()
        pygame.display.flip()

    def animate(self, anim, currentEntity):
        if anim == "right":
            self.walk_right(currentEntity)
        elif anim == "left":
            self.walk_left(currentEntity)
        elif anim == "up":
            self.walk_up(currentEntity)
        elif anim == "down":
            self.walk_down(currentEntity)
        elif anim == "die":
            self.die(currentEntity)
        pygame.display.flip()

    def render_background(self):
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

    def walk_right(self, entity):
        counter = 0
        n = 0
        while counter < 76:
            self.render_background()
            entity.displayX += entity.vel
            counter += entity.vel
            if n < 8:
                entity.char = entity.walk_right[n]
                n += 1
            else:
                n = 0
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = pygame.image.load('media/standing.png')
        

    def walk_left(self, entity):
        counter = 0
        n = 0
        while counter < 76:
            self.render_background()
            entity.displayX -= entity.vel
            counter += entity.vel
            print(counter)
            if n < 8:
                entity.char = entity.walk_left[n]
                n += 1
            else:
                n = 0
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = pygame.image.load('media/standing.png')

    def walk_up(self, entity):
        counter = 0
        while counter < 76:
            self.render_background()
            entity.displayY -= entity.vel
            counter += entity.vel
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = pygame.image.load('media/standing.png')

    def walk_down(self, entity):
        counter = 0
        while counter < 76:
            self.render_background()
            entity.displayY += entity.vel
            counter += entity.vel
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = pygame.image.load('media/standing.png')

    def die(self, entity):
        pass #death animation

import sys, pygame

class Renderer:
    def __init__(self, screen):

        self.tilewidth, self.tileheight = screen
        self.tiles = [[0] * self.tileheight for i in range(self.tilewidth)]
        self.size = self.width, self.height = self.tileheight*50, self.tilewidth*50
        self.screen = pygame.display.set_mode(self.size)
        self.square = pygame.image.load("media/grass2.png")
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
                self.squarerect.top = i*50
                self.squarerect.left = j*50
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
        while counter < 50:
            self.render_background()
            entity.displayX += entity.vel
            counter += entity.vel
            if (n < 9):
                entity.char = entity.walkRight[n]
                n += 1
            else:
                n = 0
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = entity.standing
        

    def walk_left(self, entity):
        counter = 0
        n = 0
        while counter < 50:
            self.render_background()
            entity.displayX -= entity.vel
            counter += entity.vel
            if (n < 9):
                entity.char = entity.walkLeft[n]
                n += 1
            else:
                n = 0
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = entity.standing

    def walk_up(self, entity):
        counter = 0
        n=0
        while counter < 50:
            self.render_background()
            entity.displayY -= entity.vel
            counter += entity.vel
            if n < 8:
                entity.char = entity.walkUp[n]
                n += 1
            else:
                n = 0
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = entity.standing

    def walk_down(self, entity):
        counter = 0
        n = 0
        while counter < 50:
            self.render_background()
            entity.displayY += entity.vel
            counter += entity.vel
            if (n < 9):
                entity.char = entity.walkDown[n]
                n += 1
            else:
                n = 0
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = entity.standing
        
    def die(self, entity):
        pass #death animation

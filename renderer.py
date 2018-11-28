import sys, pygame

class Renderer:
    def __init__(self, screen):

        self.tilewidth, self.tileheight = screen
        self.tiles = [[0] * self.tileheight for i in range(self.tilewidth)]
        self.size = self.width, self.height = self.tileheight*50, self.tilewidth*50
        self.screen = pygame.display.set_mode(self.size)
        self.square = pygame.image.load("media/grass.png")
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
        walkRight = [pygame.image.load('media/sprites/SwordsMan/WR/1.png'), pygame.image.load('media/sprites/SwordsMan/WR/2.png'), pygame.image.load('media/sprites/SwordsMan/WR/3.png'), pygame.image.load('media/sprites/SwordsMan/WR/4.png'), pygame.image.load('media/sprites/SwordsMan/WR/5.png'), pygame.image.load('media/sprites/SwordsMan/WR/6.png'), pygame.image.load('media/sprites/SwordsMan/WR/7.png'), pygame.image.load('media/sprites/SwordsMan/WR/8.png'), pygame.image.load('media/sprites/SwordsMan/WR/9.png')]
        counter = 0
        n = 0
        while counter < 50:
            self.render_background()
            entity.displayX += entity.vel
            counter += entity.vel
            if (n < 9):
                entity.char = walkRight[n]
                n += 1
            else:
                n = 0
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = entity.standing
        

    def walk_left(self, entity):
        walkLeft = [pygame.image.load('media/sprites/SwordsMan/WL/1.png'), pygame.image.load('media/sprites/SwordsMan/WL/2.png'), pygame.image.load('media/sprites/SwordsMan/WL/3.png'), pygame.image.load('media/sprites/SwordsMan/WL/4.png'), pygame.image.load('media/sprites/SwordsMan/WL/5.png'), pygame.image.load('media/sprites/SwordsMan/WL/6.png'), pygame.image.load('media/sprites/SwordsMan/WL/7.png'), pygame.image.load('media/sprites/SwordsMan/WL/8.png'), pygame.image.load('media/sprites/SwordsMan/WL/9.png')]
        counter = 0
        n = 0
        while counter < 50:
            self.render_background()
            entity.displayX -= entity.vel
            counter += entity.vel
            if (n < 9):
                entity.char = walkLeft[n]
                n += 1
            else:
                n = 0
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = entity.standing

    def walk_up(self, entity):
        walkUp = [pygame.image.load('media/sprites/SwordsMan/WU/1.png'), pygame.image.load('media/sprites/SwordsMan/WU/2.png'), pygame.image.load('media/sprites/SwordsMan/WU/3.png'), pygame.image.load('media/sprites/SwordsMan/WU/4.png'), pygame.image.load('media/sprites/SwordsMan/WU/5.png'), pygame.image.load('media/sprites/SwordsMan/WU/6.png'), pygame.image.load('media/sprites/SwordsMan/WU/7.png'), pygame.image.load('media/sprites/SwordsMan/WU/8.png'), pygame.image.load('media/sprites/SwordsMan/WU/9.png')]
        counter = 0
        n=0
        while counter < 50:
            self.render_background()
            entity.displayY -= entity.vel
            counter += entity.vel
            if n < 8:
                entity.char = walkUp[n]
                n += 1
            else:
                n = 0
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = entity.standing

    def walk_down(self, entity):
        walkDown = [pygame.image.load('media/sprites/SwordsMan/WD/1.png'), pygame.image.load('media/sprites/SwordsMan/WD/2.png'), pygame.image.load('media/sprites/SwordsMan/WD/3.png'), pygame.image.load('media/sprites/SwordsMan/WD/4.png'), pygame.image.load('media/sprites/SwordsMan/WD/5.png'), pygame.image.load('media/sprites/SwordsMan/WD/6.png'), pygame.image.load('media/sprites/SwordsMan/WD/7.png'), pygame.image.load('media/sprites/SwordsMan/WD/8.png'), pygame.image.load('media/sprites/SwordsMan/WD/9.png')]
        counter = 0
        n = 0
        while counter < 50:
            self.render_background()
            entity.displayY += entity.vel
            counter += entity.vel
            if (n < 9):
                entity.char = walkDown[n]
                n += 1
            else:
                n = 0
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = entity.standing
        
    def die(self, entity):
        pass #death animation

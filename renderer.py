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

    def render_title_screen(self):
        blue = 0, 0, 255
        self.screen.fill(blue)
        title_image = pygame.image.load("facts.png")
        title_image = pygame.transform.scale(title_image, (738, 415))
        castle_image = pygame.image.load("castle.jpg")
        self.screen.blit(castle_image, (0, 0))
        self.screen.blit(title_image, (0, -50))

    def renderLevelSelect(self):
        green = 0, 255, 0
        self.screen.fill(green)
        green = 0, 255, 0
        self.screen.fill(green)
        level_image = pygame.image.load("levelselect.png")
        level_image = pygame.transform.scale(level_image, (455, 137))
        first_image = pygame.image.load("mission 1.png")
        first_image = pygame.transform.scale(first_image, (249, 172))
        second_image = pygame.image.load("mission 2.png")
        second_image = pygame.transform.scale(second_image, (249, 172))
        third_image = pygame.image.load("mission 3.png")
        third_image = pygame.transform.scale(third_image, (249, 172))
        one_key = pygame.image.load("1.png")
        one_key = pygame.transform.scale(one_key, (122, 133))
        two_key = pygame.image.load("2.png")
        two_key = pygame.transform.scale(two_key, (122, 133))
        three_key = pygame.image.load("3.png")
        three_key = pygame.transform.scale(three_key, (122, 133))
        background = pygame.image.load("grass.jpg")
        background = pygame.transform.scale(background, (1443, 902))
        self.screen.blit(background, (0, 0))
        self.screen.blit(level_image, (150, 0))
        self.screen.blit(first_image, (0, 175))
        self.screen.blit(second_image, (250, 175))
        self.screen.blit(third_image, (500, 175))
        self.screen.blit(one_key, (65, 320))
        self.screen.blit(two_key, (317, 320))
        self.screen.blit(three_key, (567, 320))

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

import sys, pygame

class Renderer:
    def __init__(self, screen):

        self.tilewidth, self.tileheight = screen
        self.tiles = [[0] * self.tileheight for i in range(self.tilewidth)]
        self.size = self.width, self.height = self.tileheight*65, self.tilewidth*65
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
        elif anim == "attack":
            self.attack(currentEntity)
        elif anim == "die":
            self.die(currentEntity)
        elif anim == "win":
            self.win()
        elif anim == "lose":
            self.lose()
        pygame.display.flip()

    def render_background(self):
        black = 0, 0, 0
        self.screen.fill(black)

        for i in range(self.width):
            for j in range(self.height):
                self.squarerect.top = i*65
                self.squarerect.left = j*65
                self.screen.blit(self.square, self.squarerect)

    def render_entities(self, entities):
        for e in entities:
            e.draw(self.screen)

    def render_title_screen(self):
        blue = 0, 0, 255
        self.screen.fill(blue)
        title_image = pygame.image.load("media/menus/facts.png")
        title_image = pygame.transform.scale(title_image, (738, 415))
        castle_image = pygame.image.load("media/menus/castle.jpg")
        self.screen.blit(castle_image, (0, 0))
        self.screen.blit(title_image, (-50, -50))

    def renderLevelSelect(self):
        green = 0, 255, 0
        self.screen.fill(green)
        green = 0, 255, 0
        self.screen.fill(green)
        level_image = pygame.image.load("media/menus/levelselect.png")
        level_image = pygame.transform.scale(level_image, (455, 137))
        first_image = pygame.image.load("media/menus/mission 1.png")
        first_image = pygame.transform.scale(first_image, (191, 132))
        second_image = pygame.image.load("media/menus/mission 2.png")
        second_image = pygame.transform.scale(second_image, (191, 132))
        third_image = pygame.image.load("media/menus/mission 3.png")
        third_image = pygame.transform.scale(third_image, (191, 132))
        one_key = pygame.image.load("media/menus/1.png")
        one_key = pygame.transform.scale(one_key, (122, 133))
        two_key = pygame.image.load("media/menus/2.png")
        two_key = pygame.transform.scale(two_key, (122, 133))
        three_key = pygame.image.load("media/menus/3.png")
        three_key = pygame.transform.scale(three_key, (122, 133))
        background = pygame.image.load("media/menus/grass.jpg")
        background = pygame.transform.scale(background, (1443, 902))
        self.screen.blit(background, (0, 0))
        self.screen.blit(level_image, (90, 0))
        self.screen.blit(first_image, (0, 175))
        self.screen.blit(second_image, (230, 175))
        self.screen.blit(third_image, (450, 175))
        self.screen.blit(one_key, (35, 300))
        self.screen.blit(two_key, (270, 300))
        self.screen.blit(three_key, (490, 300))

    def walk_right(self, entity):
        counter = 0
        n = 0
        while counter < 65:
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
        while counter < 65:
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
        while counter < 65:
            self.render_background()
            entity.displayY -= entity.vel
            counter += entity.vel
            if n < 9:
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
        while counter < 65:
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

    def attack(self, entity):
        n = 0
        while n < 7:
            if (n == 6):
                entity.char = entity.standing
                pygame.display.flip()
                n += 1
            else:
                self.render_background()
                entity.char = entity.attack[n]
                entity.draw(self.screen)
                pygame.display.flip()
                n += 1
        
    def die(self, entity):
        n = 0
        while n < 7:
            if (n == 6):
                entity.char = entity.dead
                pygame.display.flip()
                n += 1
            else:
                self.render_background()
                entity.char = entity.death[n]
                entity.draw(self.screen)
                pygame.display.flip()
                n += 1

    def win(self):
        n = 0
        win = [pygame.image.load('media/win1/1.png'), pygame.image.load('media/win1/2.png'), pygame.image.load('media/win1/3.png'), pygame.image.load('media/win1/4.png'), pygame.image.load('media/win1/5.png'), pygame.image.load('media/win1/6.png'), pygame.image.load('media/win1/7.png'), pygame.image.load('media/win1/8.png'), pygame.image.load('media/win1/9.png'),pygame.image.load('media/win1/10.png'),pygame.image.load('media/win1/11.png'),pygame.image.load('media/win1/12.png'),pygame.image.load('media/win1/13.png'),pygame.image.load('media/win1/14.png'),pygame.image.load('media/win1/15.png'),pygame.image.load('media/win1/16.png'),pygame.image.load('media/win1/17.png'),pygame.image.load('media/win1/18.png'),pygame.image.load('media/win1/19.png'),]
        while n < 19:
            self.render_background()
            self.screen.blit(win[n], (0, 0))
            pygame.display.flip()
            n += 1

    def lose(self):
        n = 0
        lose = [pygame.image.load('media/lose/1.png'), pygame.image.load('media/lose/2.png'), pygame.image.load('media/lose/3.png'), pygame.image.load('media/lose/4.png'), pygame.image.load('media/lose/5.png'), pygame.image.load('media/lose/6.png'), pygame.image.load('media/lose/7.png'), pygame.image.load('media/lose/8.png'), pygame.image.load('media/lose/9.png'),pygame.image.load('media/lose/10.png'),pygame.image.load('media/lose/11.png'),pygame.image.load('media/lose/12.png'),pygame.image.load('media/lose/13.png'),pygame.image.load('media/lose/14.png'),pygame.image.load('media/lose/15.png'),pygame.image.load('media/lose/16.png'),pygame.image.load('media/lose/17.png'),pygame.image.load('media/lose/18.png'),pygame.image.load('media/lose/19.png'),]
        while n < 19:
            self.render_background()
            self.screen.blit(lose[n], (0, 0))
            pygame.display.flip()
            n += 1

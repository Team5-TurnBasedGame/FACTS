import sys, pygame, logic

class Renderer:
    def __init__(self, game):

        self.tilewidth, self.tileheight = game.stateinfo.get("screen")
        self.tiles = [[0] * self.tileheight for i in range(self.tilewidth)]
        self.size = self.width, self.height = self.tileheight*76, self.tilewidth*76
        self.screen = pygame.display.set_mode(self.size)
        self.square = pygame.image.load("square.png")
        self.squarerect = self.square.get_rect()
        self.man = game.entities[-1]
        self.game = game
        
    def render(self, game):

        self.renderBackground()
        if game.stateinfo:
            if game.stateinfo['title'] == "start":
                self.renderTitleScreen()
            elif game.stateinfo['turn'] == "select screen":
                self.renderLevelScreen()

            #elif game.stateinfo['game']
                #try:
                 #   currentAnim = tuple(self.game.animations.pop())
                  #  currentEntity = self.game.get_entity(currentAnim[1])
                   # if currentAnim[0] == "right":
                    #    self.walkRight(currentEntity)
                    #elif currentAnim[0] == "left":
                     #   self.walkLeft(currentEntity)
                    #elif currentAnim[0] == "up":
                    #    self.walkUp(currentEntity)
                    #elif currentAnim[0] == "down":
                     #   self.walkDown(currentEntity)
                      #  except:
                       #     self.man.draw(self.screen)
                        #    pygame.display.flip()

    def renderBackground(self):
        black = 0, 0, 0
        self.screen.fill(black)

        for i in range(self.width):
            for j in range(self.height):
                self.squarerect.top = i*76
                self.squarerect.left = j*76
                self.screen.blit(self.square, self.squarerect)

    def renderTitleScreen(self):
        blue = 0, 0, 255
        self.screen.fill(blue)

    def renderLeveleScreen(self):
        green = 0, 255, 0
        self.screen.fill(green)

    def walkRight(self, entity):
        counter = 0
        n = 0
        while counter < 76:
            self.renderBackground()
            entity.x += entity.vel
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
            entity.x -= entity.vel
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
            entity.y -= entity.vel
            counter += entity.vel
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = pygame.image.load('media/standing.png')

    def walkDown(self, entity):
        counter = 0
        while counter < 76:
            self.renderBackground()
            entity.y += entity.vel
            counter += entity.vel
            entity.draw(self.screen)
            pygame.display.flip()
        entity.char = pygame.image.load('media/standing.png')

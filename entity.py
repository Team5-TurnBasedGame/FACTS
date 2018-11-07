import pygame


class entity:

    position_x = 0
    position_y = 0



    def move(self, x_offset, y_offset):
        self.position_x += x_offset
        self.position_y += y_offset
        self.graphic = pygame.image.load("player.png")
        self.graphicrect = self.graphic.getrect()

    def relocate(self, new_x, new_y):
        self.position_x = new_x
        self.position_y = new_y

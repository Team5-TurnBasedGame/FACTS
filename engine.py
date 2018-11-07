import sys
import pygame
import renderer
import eventhandler
import logic
import entity
pygame.init()

n = 10
m = 10

pygame.display.set_caption("First Game")
clock = pygame.time.Clock()
game = logic.logic()
r = renderer.Renderer(game)

while 1:
    eventhandler.handle_events(game)
    # logic.resolve_changes()
    r.render()
    clock.tick(60)

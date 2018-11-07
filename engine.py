import sys
import pygame
import renderer
import eventhandler
import logic
pygame.init()

n = 10
m = 10

r = renderer.Renderer(n, m)



clock = pygame.time.Clock()

while 1:
    eventhandler.handle_events()
    logic.resolve_changes()
    r.render()
    clock.tick(15)
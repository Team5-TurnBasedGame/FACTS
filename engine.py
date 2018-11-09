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

wtev = True

while 1:
    clock.tick(27)
    eventhandler.handle_events(game)
    # logic.resolve_changes()
    r.render()
    
    if wtev:
        n = 0
        while n < 5:
            pygame.time.delay(00)
            r.walkRight()
            n +=1
        m = 0
        while m < 3:
            pygame.time.delay(00)
            r.walkLeft()
            m += 1
        a = 0
        while a < 4:
            pygame.time.delay(00)
            r.walkDown()
            a += 1
        b = 0
        while b < 3:
            pygame.time.delay(00)
            r.walkRight()
            b += 1
        c = 0
        while c < 3:
            pygame.time.delay(00)
            r.walkUp()
            c += 1
        wtev = False
    

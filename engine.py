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
game = logic.title()

walkRight = [pygame.image.load('media/R1.png'), pygame.image.load('media/R2.png'), pygame.image.load('media/R3.png'), pygame.image.load('media/R4.png'), pygame.image.load('media/R5.png'), pygame.image.load('media/R6.png'), pygame.image.load('media/R7.png'), pygame.image.load('media/R8.png'), pygame.image.load('media/R9.png')]
walkLeft = [pygame.image.load('media/L1.png'), pygame.image.load('media/L2.png'), pygame.image.load('media/L3.png'), pygame.image.load('media/L4.png'), pygame.image.load('media/L5.png'), pygame.image.load('media/L6.png'), pygame.image.load('media/L7.png'), pygame.image.load('media/L8.png'), pygame.image.load('media/L9.png')]
char = pygame.image.load('media/standing.png')
manUnit = entity.unit(walkRight, walkLeft)
man = entity.entity(game, 0, 0, 64, 64, char, manUnit)

other = entity.entity(game, 5, 0, 64, 64, char, manUnit)

game.entities.append(man)
game.entities.append(other)
game.current_entity = man

wtev = True

while (not game.quit):
    game.handle_events()
    game.resolve_changes()
    game.render()
    game = logic.updateState(game)
    clock.tick(10)
    
    if wtev:
        game.animations.append(("right", game.get_current_entity()))
        game.animations.append(("right", game.get_current_entity()))
        wtev = False

pygame.display.quit()
pygame.quit()
sys.exit()

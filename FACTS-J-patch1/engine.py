import sys
import pygame
import renderer
import eventhandler
import logic
import entity
pygame.init()


pygame.display.set_caption("First Game")
clock = pygame.time.Clock()
game = logic.Title()

wtev = False

while (not game.quit):
    game.handle_events()
    game.resolve_changes()
    game.render()
    game = logic.update_state(game)
    clock.tick(10)
    
    if wtev:
        game.animations.append(("down", game.get_current_entity()))
        game.animations.append(("down", game.get_current_entity()))
        wtev = False

pygame.display.quit()
pygame.quit()
sys.exit()

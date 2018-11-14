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
r = renderer.Renderer(game)

wtev = False

while (not game.quit):
    game.handle_events()
    game.resolve_changes()
    game = logic.updateState(game)
    clock.tick(10)
    r.render(game)
    
    if wtev:
        game.animations.append(("up", game.get_current_entity()))
        game.animations.append(("down", game.get_current_entity()))
        game.animations.append(("down", game.get_current_entity()))
        game.animations.append(("right", game.get_current_entity()))
        game.animations.append(("right", game.get_current_entity()))
        wtev = False

pygame.display.quit()
pygame.quit()
sys.exit()

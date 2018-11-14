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
game = logic.State()
r = renderer.Renderer(game)

wtev = True

while 1:
    #eventhandler.handle_events(game)
    game.stateinfo['state'].handle_events()
    State.resolve_changes()
    r.render(game)
    
    if wtev:
        game.animations.append(("up", game.get_current_entity()))
        game.animations.append(("down", game.get_current_entity()))
        game.animations.append(("down", game.get_current_entity()))
        game.animations.append(("right", game.get_current_entity()))
        game.animations.append(("right", game.get_current_entity()))
        wtev = False

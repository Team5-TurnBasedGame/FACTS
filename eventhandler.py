import sys, pygame, logic


def handle_events(game):
    if game.stateinfo:
        if game.stateinfo['title'] == "start":
            game.handle_system_events(game)
            game.handle_title_events(game)
        elif game.stateinfo['turn'] == "select screen":
            game.handle_system_events(game)
            game.handle_level_events(game)
            
def handle_system_events(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))


def handle_title_events(State, event):
    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if keys[pg.K_LEFT]:
            State.done = True
            print("left")
            State.next = 'turn'

def handle_level_events(State, event):
    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if keys[pg.K_LEFT]:
                State.done = True
                print("left")
                State.next = 'roster'

    #curr = game.get_entity(game.stateinfo["current_entity"])

    #if keys[pygame.K_LEFT] and curr.x >= curr.vel:
        #curr.x -= curr.vel
    #elif keys[pygame.K_RIGHT] and curr.x < (760 - curr.width - curr.vel):
     #   curr.x += curr.vel
    #elif keys[pygame.K_UP] and curr.y >= curr.vel:
     #   curr.y -= curr.vel
    #elif keys[pygame.K_DOWN] and curr.y < (760 - curr.height - curr.vel):
     #   curr.y += curr.vel


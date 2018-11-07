import sys, pygame


def handle_events(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    keys = pygame.key.get_pressed()

    curr = game.get_entity(game.stateinfo["current_entity"])

    if keys[pygame.K_LEFT] and curr.x > curr.vel:
        curr.x -= curr.vel
        print ("left pressed")
    elif keys[pygame.K_RIGHT] and curr.x < (760 - curr.width - curr.vel):
        curr.x += curr.vel
        print ("right pressed")
    elif keys[pygame.K_UP] and curr.y > curr.vel:
        curr.y -= curr.vel
        print ("up pressed")
    elif keys[pygame.K_DOWN] and curr.y < (760 - curr.height - curr.vel):
        curr.y += curr.vel
        print ("down pressed")


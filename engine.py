import sys, pygame, renderer, tile, player
pygame.init()

n = 10
m = 10

r = renderer.Renderer(n, m)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    r.render()

import sys, pygame
pygame.init()

black = 0, 0, 0
n = 10
m = 10
tiles = [[0] * m for i in range(n)]

size = width, height = n*76, m*76


screen = pygame.display.set_mode(size)

square = pygame.image.load("square.png")
squarerect = square.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        
    print(squarerect.width)
    print(squarerect.height)

        
    screen.fill(black)
    
    for i in range(n):
        for j in range(m):
            squarerect.top = i*76
            squarerect.left = j*76
            screen.blit(square, squarerect)
    pygame.display.flip()
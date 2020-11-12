import sys, pygame
pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font('freesansbold.ttf', 32)
white = (255, 255, 255)
black = (0, 0, 0)
gametext = font.render('push the arrow keys', True, white)
gametextrect = gametext.get_rect()
gametextrect.topleft = (0, 0)
ship = pygame.image.load('space ship_0.png')
shiprect = ship.get_rect()
shiprect.center = (300, 300)
shipdx = 0
shipdy = 0
shipspeed = 2

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                shipdx = shipspeed
            elif event.key == pygame.K_DOWN:
                shipdy = shipspeed
            elif event.key == pygame.K_LEFT:
                shipdx = -shipspeed
            elif event.key == pygame.K_UP:
                shipdy = -shipspeed
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                shipdx = 0
            elif event.key in (pygame.K_DOWN, pygame.K_UP):
                shipdy = 0
    shiprect.x = shiprect.x + shipdx
    shiprect.y = shiprect.y + shipdy
    if shiprect.x > width:
        shiprect.x = 0
    elif shiprect.x < 0:
        shiprect.x = width
    if shiprect.y > height:
        shiprect.y = 0
    elif shiprect.y < 0:
        shiprect.y = height
    screen.fill(black)
    screen.blit(gametext, gametextrect)
    screen.blit(ship, shiprect)
    pygame.display.update()
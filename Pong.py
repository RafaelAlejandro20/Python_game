import pygame, sys, random
pygame.init()

Black   =   (0,0,0)
White   =   (255,255,255)
Red     =   (255,0,0)
Green   =   (0,255,0)
Blue    =   (0,0,255)

size = (400,600)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

game_over = False
coord_x1 = 150
coord_y1 = 560
speed_x1 = 0
speed_y1 = 0
coord_x2 = 150
coord_y2 = 20
speed_x2 = 0
speed_y2 = 0
pelota_x = 195
pelota_y = 300
pelota_speed_x = 2
pelota_speed_y = 2

background = pygame.image.load("Pista.png").convert()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x1 = -4
            if event.key == pygame.K_RIGHT:
                speed_x1 = 4
            if event.key == pygame.K_a:
                speed_x2 = -4
            if event.key == pygame.K_d:
                speed_x2 = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x1 = 0
            if event.key == pygame.K_RIGHT:
                speed_x1 = 0
            if event.key == pygame.K_a:
                speed_x2 = 0
            if event.key == pygame.K_d:
                speed_x2 = 0

    if pelota_y > 600:
        pelota_x = 195
        pelota_y = 300
        pelota_speed_x *= -1
        pelota_speed_y *= -1
    if pelota_y < 0:
        pelota_x = 195
        pelota_y = 300
        pelota_speed_x *= -1
        pelota_speed_y *= -1

    if coord_x1 < 0:
        speed_x1 = 4
    elif coord_x1 > 300:
        speed_x1 = -4
    if coord_x2 < 0:
        speed_x2 = 4
    elif coord_x2 > 300:
        speed_x2 = -4

    screen.blit(background,[0,0])

    if pelota_x > 390 or pelota_x < 10:
        pelota_speed_x *= -1
    coord_x1 += speed_x1
    coord_x2 += speed_x2
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y
    pelota = pygame.draw.circle(screen,White,(pelota_x,pelota_y),10)
    jugador1 = pygame.draw.rect(screen,White,(coord_x1,coord_y1,100,20),0,10)
    jugador2 = pygame.draw.rect(screen,White,(coord_x2,coord_y2,100,20),0,10)

    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_y *= -1

    pygame.display.flip()
    clock.tick(60)
pygame.QUIT()
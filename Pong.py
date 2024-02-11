import pygame, sys, random
pygame.init()

Black = (0,0,0)
White = (255,255,255)

#tamano de pantalla
size = (400,600)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

game_over = False
mensaje = False

#variables
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
pelota_speed_x = 3
pelota_speed_y = 3

contador = 0

font = pygame.font.SysFont("Carlito",40)
text = font.render("GAME OVER",True,White)

background = pygame.image.load("Pista.png").convert()
img_pelota = pygame.image.load("Pelota.png").convert()
img_pelota.set_colorkey([0,0,0])

sound = pygame.mixer.Sound("game_over.ogg")
ping_pong = pygame.mixer.Sound("ping_pong.ogg")

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
            if event.key == pygame.K_r:
                mensaje = False
                pelota_speed_x = 3
                pelota_speed_y = 3
                contador = 0

    if pelota_y > 600 or pelota_y < -20:
        sound.play()
        coord_x1 = 150
        coord_x2 = 150
        pelota_x = 190
        pelota_y = 290
        pelota_speed_x = 0
        pelota_speed_y = 0
        mensaje = True

    if coord_x1 < 0:
        speed_x1 = 4
    elif coord_x1 > 300:
        speed_x1 = -4
    if coord_x2 < 0:
        speed_x2 = 4
    elif coord_x2 > 300:
        speed_x2 = -4

    screen.blit(background,[0,0])
    if mensaje == True:
        speed_x1 = 0
        speed_x2 = 0
        screen.blit(text,[100,150])

    coord_x1 += speed_x1
    coord_x2 += speed_x2

    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y
        
    pelota = screen.blit(img_pelota,[pelota_x,pelota_y])

    if pelota_x > 380 or pelota_x < 0:
        pelota_speed_x *= -1

    jugador1 = pygame.draw.rect(screen,White,(coord_x1,coord_y1,100,20),0,10)
    jugador2 = pygame.draw.rect(screen,White,(pelota_x-40,coord_y2,100,20),0,10)

    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_y *= -1
        ping_pong.play()
        contador = contador + 1

    cont = font.render("{}".format(contador),True,White)
    screen.blit(cont,[190,420])

    pygame.display.flip()
    clock.tick(60)
#pygame.QUIT()
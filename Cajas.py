import pygame, sys, random
pygame.init()

#Definir colores
Black   =   (0,0,0)
White   =   (255,255,255)
Red     =   (255,0,0)
Green   =   (0,255,0)
Blue    =   (0,0,255)

size = (800,500)

#Crear ventana
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

coord_x = 0
coord_y = 0

speed_x = 0
speed_y = 0

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -4
            if event.key == pygame.K_RIGHT:
                speed_x = 4
            if event.key == pygame.K_UP:
                speed_y = -4
            if event.key == pygame.K_DOWN:
                speed_y = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_UP:
                speed_y = 0
            if event.key == pygame.K_DOWN:
                speed_y = 0
    screen.fill(White)
    coord_x += speed_x
    coord_y += speed_y
    pygame.draw.rect(screen,Blue,(coord_x,coord_y,20,20))
    pygame.display.flip()
    clock.tick(60)
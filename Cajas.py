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

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(White)
    mouse = pygame.mouse.get_pos()
    x = mouse[0]
    y = mouse[1]
    pygame.draw.rect(screen,Blue,(x,y,20,20))
    pygame.display.flip()
    clock.tick(60)
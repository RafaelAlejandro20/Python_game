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

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    
    screen.fill(White)
    pygame.display.flip()
    clock.tick(60)
import pygame, sys
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

coordx = 0
coordy = 0

speedx = 1
speedy = 1

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    if (coordx > 720):
        speedx += -1
    elif(coordx < 0):
        speedx += +1
    
    if (coordy > 420):
        speedy += -1
    elif(coordy < 0):
        speedy += +1

    coordx += speedx
    coordy += speedy
    screen.fill(White)
    #pygame.draw.line(screen,Green,[0,40],[800,40],1)
    #pygame.draw.rect(screen,Black,(0,0,800,40))
    #pygame.draw.circle(screen,Red,(100,100),50)
    #for i in range(0,800,100):
    #    pygame.draw.rect(screen,Black,(i,0,100,100))
    pygame.draw.rect(screen,Red,(coordx,coordy,80,80),0,5)
    pygame.display.flip()
    clock.tick(60)
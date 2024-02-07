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

coordx = 0
coordy = 0

speedx = 1
speedy = 1

coor_list = []
for i in range(60):
    x = random.randint(0,800)
    y = random.randint(0,500)
    coor_list.append([x,y])

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    #if (coordx > 720):
    #    speedx += -1
    #elif(coordx < 0):
    #    speedx += +1
    
    #if (coordy > 420):
    #    speedy += -1
    #elif(coordy < 0):
    #    speedy += +1

    screen.fill(White)
    for j in coor_list:
        pygame.draw.circle(screen,Blue,j,2)
        j[1] += 1
        if j[1] > 500:
            j[1] = 0
    #coordx += speedx
    #coordy += speedy
    #screen.fill(White)
    #pygame.draw.rect(screen,Red,(coordx,coordy,80,80),0,5)
    pygame.display.flip()
    clock.tick(60)
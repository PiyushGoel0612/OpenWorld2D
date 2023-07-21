import pygame
import a2

"""
0 = empty..1 = ground..2 = platforms
30x30 sizes
"""

lvl1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,2,2],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,2,2,2,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1],
        [1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1]]
colr = ["Blue","Green","Brown"]   
flr = len(lvl1)

ground = []
platf = []

pygame.init()

clock = pygame.time.get_ticks()
clock1 = pygame.time.Clock()

screen = pygame.display.set_mode((480,380))

run = True
start = 4
m = a2.Mario(160,280)
offset =  0

while run:
    pygame.event.get()
                     
    clock1.tick(60)

    screen.fill("Green")
    ind = 0
    line = 0

    m.move(480)
    offset += -m.dx
    if m.dx > 0:
        if (offset / -40 > 1):
            offset = -2
            start += 1
    elif m.dx < 0:
        if start > 0:
            if (offset / 40 > 1):
                offset = 2
                start -= 1
     
    ground = []
    platf = []
    for i in lvl1:
        for j in i[start:start+14]:
            if (line == (flr - 2)) and (j == 1) and ((ind > 3) and (ind < 7)):
                ground.append(pygame.draw.rect(screen,colr[j],pygame.Rect(ind*40-40+offset,line*40,40,40)))
            elif (j == 2) and ((ind > 3) and (ind < 7)):
                platf.append(pygame.draw.rect(screen,colr[j],pygame.Rect(ind*40-40+offset,line*40,40,40)))
            else:
                pygame.draw.rect(screen,colr[j],pygame.Rect(ind*40-40+offset,line*40,40,40))
            ind += 1
        line += 1
        ind = 0

    m.jump(ground,platf)

    pygame.draw.rect(screen,"White",m.rect)

    tm = pygame.time.get_ticks()
    if tm - clock > 15000:
        run = False
  
    pygame.display.update()

pygame.quit()
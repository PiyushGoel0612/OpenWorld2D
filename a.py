import pygame
import a2

"""
0 = empty ; 1 = ground ; 2 = platforms
3 = enemy ;
"""

lvl1 = [[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,3,0,0,0,2,2,2,0,0,0,0,0,0,2,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,1,0,0,0,0,3,0,1,1,1,1,0,0,1,1],
        [1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1]]

ln = len(lvl1[0])

colr = ["Blue","Green","Brown","Orange"]   
flr = len(lvl1)

ground = []
platf = []
enemy = []

pygame.init()

clock = pygame.time.get_ticks()
clock1 = pygame.time.Clock()

screen = pygame.display.set_mode((650,475))

run = True
start = 4
m = a2.Mario(200,350)
offset =  0

while run:
     
    pygame.event.get()
    clock1.tick(60)

    screen.fill("Green")
    ind = 0
    line = 0

    m.move(ground,platf,ln,offset,start)
    offset += -m.dx
    if m.dx > 0:
        if (offset / -50 > 1):
            offset = -2
            start += 1
    elif (m.dx < 0):
        if start > 0:
            if (offset / 50 > 1):
                offset = 2
                start -= 1
    
    if m.dx != 0:
        for i in enemy:
            i[0].rect.x -= m.dx

            if i[0].rect.x - m.rect.x > 700:
                lvl1[i[1][0]][i[1][1]] = 3
                enemy.remove(i)
            elif m.rect.x - i[0].rect.x > 500:
                lvl1[i[1][0]][i[1][1]] = 3
                enemy.remove(i)
      
    ground = []
    platf = []
    for i in lvl1:
        for j in i[start:start+15]:
            if (j == 1) and ((ind > 3) and (ind < 7)):
                ground.append(pygame.draw.rect(screen,colr[j],pygame.Rect(ind*50-50+offset,line*50,50,50)))
            elif (j == 2) and ((ind > 3) and (ind < 7)):
                platf.append(pygame.draw.rect(screen,colr[j],pygame.Rect(ind*50-50+offset,line*50,50,50)))
            else:
                if j == 3:
                    post = [lvl1.index(i),i.index(j)]

                    x = lvl1.index(i)
                    y = i.index(j)
                    dets = [0,0]
                    for j in range(1,8):
                        if lvl1[x+1][y+j] == 0:
                            dets[0] = j*50 - 50
                            break
                        elif (lvl1[x][y+j] == 1) or (lvl1[x][y+j] == 2):
                            dets[0] = j*50 - 50
                            break
                    for j in range(1,8):
                        if lvl1[x+1][y-j] == 0:
                            dets[1] = j*50 - 50
                            break
                        elif (lvl1[x][y-j] == 1) or (lvl1[x][y-j] == 2):
                            dets[1] = j*50 + 50
                            break

                    enemy.append([a2.Enemy(ind*50-50+offset,line*50,dets),post])

                    lvl1[x][y] = 0
                else:
                    pygame.draw.rect(screen,colr[j],pygame.Rect(ind*50-50+offset,line*50,50,50))
            ind += 1
        line += 1
        ind = 0

    for i in enemy:
        i[0].move()
        pygame.draw.rect(screen,colr[3],pygame.Rect(i[0].rect.x,i[0].rect.y,50,50))

    m.jump(ground,platf)

    pygame.draw.rect(screen,"White",m.rect)

    if m.rect.y > 500:
        run = False
  
    pygame.display.update()

pygame.quit()
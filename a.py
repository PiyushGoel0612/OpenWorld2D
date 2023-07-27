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
lives = 3

colr = ["#3498DB","#2ECC71","#6E2C00","#F1C40F"]   
flr = len(lvl1)

ground = []
platf = []
enemy = []
blt = []

pygame.init()

clock = pygame.time.get_ticks()
clock1 = pygame.time.Clock()

screen = pygame.display.set_mode((650,475))

run = True
start = 4
m = a2.Mario(200,350)
offset =  0
i_can = 0
tmr = 0

while run:
     
    pygame.event.get()
    clock1.tick(60)

    screen.fill("#2ECC71")
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
            if (j == 1):
                ground.append(pygame.draw.rect(screen,colr[j],pygame.Rect(ind*50-50+offset,line*50,50,50)))
            elif (j == 2):
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

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if m.jmp_count:
                    i_can = 1
            elif event.key == pygame.K_RSHIFT:
                if len(blt) == 0:
                    blt.append(a2.Bullet(m.rect.x,m.rect.y+20,m.Facing))

    m.jump(ground,platf,i_can)
    m.shoot(m.rect)

    i_can = 0

    pygame.draw.rect(screen,"#283747",m.rect)

    if m.rect.y > 500:
        run = False

    if m.velocity == -1:
        for i in enemy:
            if tmr == 0:
                if m.rect.colliderect(i[0].rect):
                    lives -= 1
                    tmr = 120
    elif m.velocity < -1:
        for i in enemy:
            if m.rect.colliderect(i[0].rect):
                enemy.remove(i)

    for i in blt:
        if i.rect.x - i.srt > 500:
            blt.remove(i)
        elif i.srt - i.rect.x > 300:
            blt.remove(i)
        else:
            i.move()
            pygame.draw.rect(screen,"#A6ACAF",i)

    for i in ground:
        if len(blt) != 0:
            if i.colliderect(blt[0]):
                lvl1[int(i.y / 50)][int((i.x-offset+50)/50 + start)] = 0
                ground.remove(i)
                blt = []

    for i in platf:
        if len(blt) != 0:
            if i.colliderect(blt[0]):
                lvl1[int(i.y / 50)][int((i.x-offset+50)/50 + start)] = 0
                platf.remove(i)
                blt = []
    
    for i in enemy:
        if len(blt) != 0:
            if i[0].rect.colliderect(blt[0]):
                enemy.remove(i)
                blt = []

    for i in range(0,lives):
        pygame.draw.rect(screen,"#E74C3C",pygame.Rect(30+50*i,30,25,25))

    if tmr != 0:
        tmr -= 1

    if lives == 0:
        run = False
  
    pygame.display.update()

pygame.quit()
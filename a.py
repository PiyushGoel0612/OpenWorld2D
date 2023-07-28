import pygame
import a2

"""
0 = empty ; 1 = ground ; 2 = platforms
3 = enemy ; 4 = Gifts
lvl1 should always have 10 lists inside of it
"""

lvl1 = [[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,3,0,0,0,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,3,0,0,0,0,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,2,2,2,2,2,0,0,1,1,1,1,1]]

ln = len(lvl1[0])
lives = 3

colr = ["#3498DB","#2ECC71","#6E2C00","#F1C40F","#8E44AD"]   
flr = len(lvl1)

ground = []
platf = []
enemy = []
blt = []
gft = []

pygame.init()

clock = pygame.time.get_ticks()
clock1 = pygame.time.Clock()

screen = pygame.display.set_mode((650,475))
pygame.display.set_caption("OPEN 2D GAME")

run = True
start = 4
m = a2.Mario(200,350)
offset =  0
i_can = 0
tmr = 0
bullet_count = 3

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
    gft = []
    for i in lvl1:
        for j in i[start:start+15]:
            if (j == 1):
                ground.append(pygame.draw.rect(screen,colr[j],pygame.Rect(ind*50-50+offset,line*50,50,50)))
            elif (j == 2):
                platf.append(pygame.draw.rect(screen,colr[j],pygame.Rect(ind*50-50+offset,line*50,50,50)))
            elif j == 3:
                post = [lvl1.index(i),i.index(j)]

                x = lvl1.index(i)
                y = i.index(j)
                dets = [0,0]
                for j in range(1,8):
                    if (lvl1[x+1][y+j] == 0) or ((lvl1[x][y+j] == 1) or (lvl1[x][y+j] == 2)):
                        dets[0] = j*50 - 50
                        break
                for j in range(1,8):
                    if lvl1[x+1][y-j] == 0:
                        dets[1] = j*50 - 50
                        break
                    elif (lvl1[x][y-j] == 1) or (lvl1[x][y-j] == 2):
                        dets[1] = j*50 - 50
                        break

                enemy.append([a2.Enemy(ind*50-50+offset,line*50,dets),post])

                lvl1[x][y] = 0

            elif j == 4:
                gft.append(a2.Gift(ind*50-50+offset,line*50 + 10))

            else:
                pygame.draw.rect(screen,colr[j],pygame.Rect(ind*50-50+offset,line*50,50,50))

            ind += 1
        line += 1
        ind = 0

    for i in gft:
        
        if i.rect.colliderect(m.rect):
            pygame.draw.rect(screen,colr[0],(i.rect.x,i.rect.y - 10,50,50))
            i.reward()
            if i.prize == 1:
                bullet_count += 3
            else:
                lives += 1
            gft.remove(i)
            lvl1[int((i.rect.y/50))][int((i.rect.x-offset+50)/50 + start)] = 0
        else:
            pygame.draw.rect(screen,colr[0],(i.rect.x,i.rect.y - 10,50,50))
            pygame.draw.rect(screen,colr[4],i.rect)



    for i in enemy:
        i[0].move()

        if (i[0].rect.x - offset) % 50 == 0:
            if lvl1[int((i[0].rect.y/50)+1)][int((i[0].rect.x-offset+50)/50 + start)] == 0:
                enemy.remove(i)

        pygame.draw.rect(screen,colr[3],pygame.Rect(i[0].rect.x,i[0].rect.y,50,50))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if m.jmp_count:
                    i_can = 1
            elif event.key == pygame.K_RSHIFT:
                if (len(blt) == 0) and (bullet_count > 0):
                    blt.append(a2.Bullet(m.rect.x,m.rect.y+20,m.Facing))
                    bullet_count -= 1

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

    for i in range(0,bullet_count):
        pygame.draw.rect(screen,"#A6ACAF",pygame.Rect(30+15*i,80,5,30))

    if tmr != 0:
        tmr -= 1

    if lives == 0:
        run = False
  
    pygame.display.update()

pygame.quit()
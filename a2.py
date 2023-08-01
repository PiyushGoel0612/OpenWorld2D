import pygame
import random as rd

class Mario:

    def __init__(self,x,y):

        self.rect = pygame.Rect(x,y,50,50)
        self.rect_dwn = pygame.Rect(x,y+50,50,50)
        self.dx = 0
        self.tmr = 0
        self.velocity = 0
        self.accn = 0
        self.jmp_count = 2
        self.Facing = 'Right'
    
    def move(self,ground,platf,ln,offset,start):

        self.dx = 0
        pressed_key = pygame.key.get_pressed()
        
        if pressed_key[pygame.K_LEFT]:
            
            if (offset < 98):
                self.rect.x -= 2
                gnd_c = self.rect.collidelist(ground)
                ptf_c = self.rect.collidelist(platf)
                self.rect.x += 2

                if ptf_c != -1:
                    self.dx = 0
                elif gnd_c != -1:
                    self.dx = 0
                else:
                    self.dx = -2
                self.Facing = "Left"

        elif pressed_key[pygame.K_RIGHT]:

            if (start < ln - 6):
                self.rect.x += 2
                gnd_c = self.rect.collidelist(ground)
                ptf_c = self.rect.collidelist(platf)
                self.rect.x -= 2

                if ptf_c != -1:
                    self.dx = 0
                elif gnd_c != -1:
                    self.dx = 0
                else:
                    self.dx = 2
            self.Facing = "Right"

    def jump(self,ground,platf,i_can):
            
        if self.velocity <= 0:
            self.rect.y += 2
            gnd_c = self.rect.collidelist(ground)
            ptf_c = self.rect.collidelist(platf)
            self.rect.y -= 2

            if i_can:
                self.accn = 2
                if self.velocity < 0:
                    self.velocity = 12
                else:
                    self.velocity += 10
                self.jmp_count -= 1

            if ptf_c != -1:
                if self.velocity >= 0:
                    self.rect.y -= self.velocity - self.accn
                    self.tmr += 1
                    
                    if self.tmr % 2 == 0:
                        self.velocity -= 1
                else:
                    self.rect.y = platf[ptf_c].y - 50
                    self.jmp_count = 2
                    self.velocity = -1

            elif gnd_c != -1:
                if self.velocity >= 0:
                    self.rect.y -= self.velocity - self.accn
                    self.tmr += 1
                        
                    if self.tmr % 2 == 0:
                        self.velocity -= 1
                else:
                    self.rect.y = ground[gnd_c].y - 50
                    self.jmp_count = 2
                    self.velocity = -1

            else:
                self.rect.y -= self.velocity - self.accn
                self.tmr += 1
                    
                if self.tmr % 2 == 0:
                    self.velocity -= 1
        else:
            self.rect.y -= 2
            gnd_c = self.rect.collidelist(ground)
            ptf_c = self.rect.collidelist(platf)
            self.rect.y += 2

            if i_can:
                self.accn = 2
                if self.velocity < 0:
                    self.velocity = 12
                else:
                    self.velocity += 10
                self.jmp_count -= 1

            if ptf_c != -1:
                self.velocity = 0
                self.rect.y = self.rect.y + 50 - (self.rect.y % 50)
                return ptf_c

            elif gnd_c != -1:
                self.velocity = 0
                self.rect.y = self.rect.y + 50 - (self.rect.y % 50)

            else:
                self.rect.y -= self.velocity - self.accn
                self.tmr += 1
                    
                if self.tmr % 2 == 0:
                    self.velocity -= 1

    def shoot(self,rct):
        for k in pygame.event.get():
            if k.type == pygame.KEYDOWN:
                if k.key == pygame.K_RSHIFT:
                    print("PRESSED")

class Enemy:
    def __init__(self,x,y,dets):

        self.rect = pygame.Rect(x,y,50,50)
        self.dirtn = "right"
        self.right = dets[0]
        self.left = dets[1]

    def move(self):
        if self.dirtn == "right":
            if self.right > 0:
                self.rect.x += 2
                self.right -= 2
                self.left += 2
            else:
                self.dirtn = "left"
        
        elif self.dirtn == "left":
            if self.left > 0:
                self.rect.x -= 2
                self.left -= 2
                self.right += 2
            else:
                self.dirtn = "right"

class Bullet:

    def __init__(self,x,y,Facing):
        self.rect = pygame.Rect(x,y,30,5)
        self.Facing = Facing
        self.srt = x

    def move(self):
        if self.Facing == "Right":
            self.rect.x += 4
        else:
            self.rect.x -= 4

class Gift:

    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,40,40)
        self.prize = 0   # 0 = Nothing; 1 = bulletx3; 2 = life+1

    def reward(self):
        self.prize = rd.choice([1,2])
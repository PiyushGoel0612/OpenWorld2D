import pygame

class Mario:

    def __init__(self,x,y):

        self.rect = pygame.Rect(x,y,40,40)
        self.rect_dwn = pygame.Rect(x,y+40,40,40)
        self.dx = 0
        self.tmr = 0
        self.velocity = 0
        self.accn = 0
        self.jmp_count = 2
    
    def move(self,screen_width):

        self.dx = 0
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT]:
            self.dx = -2
        elif pressed_key[pygame.K_RIGHT]:
            self.dx = 2

    def jump(self,ground,platf):
        self.rect.y += 2
        gnd_c = self.rect.collidelist(ground)
        ptf_c = self.rect.collidelist(platf)
        self.rect.y -= 2

        if self.jmp_count:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
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
                
                if self.tmr % 3 == 0:
                    self.velocity -= 1
            else:
                self.rect.y = platf[ptf_c].y - 40
                self.jmp_count = 2

        elif gnd_c != -1:
            if self.velocity >= 0:
                self.rect.y -= self.velocity - self.accn
                self.tmr += 1
                    
                if self.tmr % 3 == 0:
                    self.velocity -= 1
            else:
                self.rect.y = ground[gnd_c].y - 40
                self.jmp_count = 2

        else:
            self.rect.y -= self.velocity - self.accn
            self.tmr += 1
                
            if self.tmr % 2 == 0:
                self.velocity -= 1
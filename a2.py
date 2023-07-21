import pygame

class Mario:

    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,40,40)
        self.dx = 0
    
    def move(self,screen_width):
        self.dx = 0
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT]:
            self.dx = -2
        elif pressed_key[pygame.K_RIGHT]:
            self.dx = 2
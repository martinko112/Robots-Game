import pygame,sys
from settings import *
from game_map import *
from assets import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, size, type):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(assets["enemy"]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size[0], size[1]))

        self.rect = self.image.get_rect(topleft = pos)

        self.defaultx = pos[0]

        if type == 2:
            self.move = 50
        if type == 3:
            self.move = 100
        
        self.direction = 0

    def update(self, shift_amount):
        self.rect.x += shift_amount
        self.defaultx += shift_amount

        if self.rect.x <= self.defaultx:
            self.direction = 2
        elif self.rect.x >= self.defaultx + self.move:
            self.direction = -2
        
        self.rect.x += self.direction
        
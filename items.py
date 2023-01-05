import pygame

from settings import *


class Drop(pygame.sprite.Sprite):
    def __init__(self, screen, pos, enemy_exp, enemy_rank):
        super(Drop, self).__init__()
        self.screen = screen
        self.exp = enemy_exp
        self.type = 'drop'
        if enemy_rank == 'common':
            if enemy_exp == 10:
                self.image = crystals[0]
                self.type = 'crystal'
            elif enemy_exp == 100:
                self.image = crystals[1]
                self.type = 'crystal'
        elif enemy_rank == 'boss':
            self.image = chest
            self.type = 'chest'
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = pos

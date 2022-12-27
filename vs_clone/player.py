from settings import *
import pygame
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Player, self).__init__()
        self.screen = screen
        self.image = player_sprites_R[0]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.health = 100
        self.kill_count_exp = 0
        self.lvl = 1
        self.exp = 100 * self.lvl
        self.angle = player_angle

    @property
    def pos(self):
        return self.rect.x, self.rect.y

    def update(self, anim_count_player):
        if self.angle == 0:
            self.image = player_sprites_R[anim_count_player // 10]
        if self.angle == 180:
            self.image = player_sprites_L[anim_count_player // 10]
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.rect.centery += player_speed
        if keys[pygame.K_w]:
            self.rect.centery -= player_speed
        if keys[pygame.K_d]:
            self.angle = 0
            self.rect.centerx += player_speed
        if keys[pygame.K_a]:
            self.rect.centerx -= player_speed
            self.angle = 180

    def draw(self):
        self.screen.blit(self.image, self.rect)

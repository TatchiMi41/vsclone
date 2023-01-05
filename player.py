from settings import *
import pygame
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Player, self).__init__()
        self.screen = screen
        self.image = player_sprites_R[0]
        self.rect = self.image.get_bounding_rect()
        self.screen_rect = screen.get_bounding_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.kill_count_exp = 0
        self.lvl = 1
        self.exp = 100 * self.lvl
        self.angle = player_angle
        self.hp_bar_height = 10
        self.hp_bar_width = 100
        self.kills = 0
        self.health_lvl = 0
        self.speed_lvl = 0
        self.speed = player_speed * player_speed_multiplier[self.speed_lvl]
        self.health = 100 * player_health_multiplier[self.health_lvl]


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
            self.rect.centery += self.speed
        if keys[pygame.K_w]:
            self.rect.centery -= self.speed
        if keys[pygame.K_d]:
            self.angle = 0
            self.rect.centerx += self.speed
        if keys[pygame.K_a]:
            self.rect.centerx -= self.speed
            self.angle = 180
        self.exp = 100 * self.lvl

    def draw_hp_bar(self, screen):
        fill = (self.health / 100) * self.hp_bar_width
        outline_rect = pygame.Rect(self.rect.x, self.rect.y, self.hp_bar_width, self.hp_bar_height)
        fill_rect = pygame.Rect(self.rect.x, self.rect.y, fill, self.hp_bar_height)
        pygame.draw.rect(screen, GREEN, fill_rect)
        pygame.draw.rect(screen, WHITE, outline_rect, 2)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update_upgrades(self, player_health_multiplier):
        self.health = 100 * player_health_multiplier[self.health_lvl]


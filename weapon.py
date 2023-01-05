from enemy import *
import pygame


class Whip(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        super(Whip, self).__init__()
        self.title = 'Whip'
        self.activate = True
        self.icon = whip_icon
        self.screen = screen
        self.image = attack_sprites_R
        self.rect = self.image.get_bounding_rect()
        self.rect.centerx, self.rect.centery = player.pos
        self.damage = 100
        self.lvl = 0

    def update(self, player, anim_count_whip):
        self.rect.centery = player.rect.centery
        if player.angle == 0:
            self.rect.centerx = player.rect.centerx + 80
            self.image = attack_sprites_R
            if 0 <= anim_count_whip < 2:
                self.image = pygame.transform.smoothscale(self.image, (37, 6))
                self.rect = self.image.get_bounding_rect()
                self.rect.centery = player.rect.centery
                self.rect.centerx = player.rect.centerx + 80
            if 1 < anim_count_whip < 4:
                self.image = pygame.transform.smoothscale(self.image, (74, 12))
                self.rect = self.image.get_bounding_rect()
                self.rect.centery = player.rect.centery
                self.rect.centerx = player.rect.centerx + 80
            if 3 < anim_count_whip < 5:
                self.image = pygame.transform.smoothscale(self.image, (110, 18))
                self.rect = self.image.get_bounding_rect()
                self.rect.centery = player.rect.centery
                self.rect.centerx = player.rect.centerx + 80
            if 4 < anim_count_whip < 6:
                self.image = pygame.transform.smoothscale(self.image, (147, 22))
                self.rect = self.image.get_bounding_rect()
                self.rect.centery = player.rect.centery
                self.rect.centerx = player.rect.centerx + 80
            if 8 < anim_count_whip < 101:
                self.image = pygame.transform.smoothscale(self.image, (0, 0))
                self.rect = self.image.get_bounding_rect()
                self.rect.centery = player.rect.centery
                self.rect.centerx = player.rect.centerx + 80
        else:
            self.rect.centerx = player.rect.x - 100
            self.image = attack_sprites_L
            if 0 <= anim_count_whip < 2:
                self.image = pygame.transform.smoothscale(self.image, (37, 6))
                self.rect = self.image.get_bounding_rect()
                self.rect.centery = player.rect.centery
                self.rect.centerx = player.rect.centerx - 90
            if 1 < anim_count_whip < 4:
                self.image = pygame.transform.smoothscale(self.image, (74, 12))
                self.rect = self.image.get_bounding_rect()
                self.rect.centery = player.rect.centery
                self.rect.centerx = player.rect.centerx - 90
            if 3 < anim_count_whip < 5:
                self.image = pygame.transform.smoothscale(self.image, (110, 18))
                self.rect = self.image.get_bounding_rect()
                self.rect.centery = player.rect.centery
                self.rect.centerx = player.rect.centerx - 90
            if 4 < anim_count_whip < 6:
                self.image = pygame.transform.smoothscale(self.image, (147, 22))
                self.rect = self.image.get_bounding_rect()
                self.rect.centery = player.rect.centery
                self.rect.centerx = player.rect.centerx - 90
            if 8 < anim_count_whip < 101:
                self.image = pygame.transform.smoothscale(self.image, (0, 0))
                self.rect = self.image.get_bounding_rect()
                self.rect.centery = player.rect.centery
                self.rect.centerx = player.rect.centerx - 90

    def draw(self):
        self.screen.blit(self.image, (self.rect.centerx, self.rect.centery))


class Garlic(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        super(Garlic, self).__init__()
        self.title = 'Garlic'
        self.activate = False
        self.icon = garlic_icon
        self.screen = screen
        self.image = garlic_spite
        self.rect = self.image.get_bounding_rect()
        self.rect.centerx, self.rect.centery = player.pos
        self.damage = 100
        self.lvl = 0

    def update(self, player, anim_count_garlic):
        self.rect.centerx, self.rect.centery = player.pos
        if 0 <= anim_count_garlic < 11 or 80 < anim_count_garlic < 101:
            self.image.set_alpha(90)
        if 10 < anim_count_garlic < 21:
            self.image.set_alpha(75)
        if 20 < anim_count_garlic < 61:
            self.image.set_alpha(60)
        if 60 < anim_count_garlic < 81:
            self.image.set_alpha(75)

    def draw(self):
        self.screen.blit(self.image, (self.rect.x + 20, self.rect.y + 20))

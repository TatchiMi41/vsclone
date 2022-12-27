from enemy import *


class Whip(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        super(Whip, self).__init__()
        self.screen = screen
        self.image = attack_sprites_R
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = player.pos
        self.damage = 100
        self.delay_to_attack = 1500

    def update(self, player):
        self.rect.centery = player.rect.centery
        if player.angle == 0:
            self.rect.centerx = player.rect.centerx + 130
            self.image = attack_sprites_R
        else:
            self.rect.centerx = player.rect.x - 100
            self.image = attack_sprites_L

    def drawing(self):
        pygame.time.wait(500)
        self.screen.blit(self.image, (self.rect.centerx, self.rect.centery))


class Garlic(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        super(Garlic, self).__init__()
        self.activate = False
        self.screen = screen
        self.image = garlic_spite
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = player.pos
        self.damage = 10
        self.lvl = 0

    def update(self, player):
        self.rect.centerx, self.rect.centery = player.pos

    def drawing(self):
        self.screen.blit(self.image, (self.rect.x+20, self.rect.y+20))

from settings import *
import math
import random


class Bat(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Bat, self).__init__()
        self.screen = screen
        self.image = bat_sprites_R[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice([random.randint(1281, 1300), random.randint(1159, 1279) - 1280])
        self.rect.centery = random.choice([random.randint(721, 760), random.randint(619, 719) - 720])
        self.damage = 1
        self.exp = 10
        self.health = 100
        self.rank = 'common'

    @property
    def pos(self):
        return float(self.rect.centerx), float(self.rect.centery)

    def update(self, player, anim_count_bat):
        if self.rect.centerx > player.rect.centerx:
            self.image = bat_sprites_R[int(anim_count_bat // 10)]
        else:
            self.image = bat_sprites_L[int(anim_count_bat // 10)]
        delta_x = player.rect.centerx - self.rect.centerx
        delta_y = player.rect.centery - self.rect.centery
        enemy_move_x = abs(delta_x) > abs(delta_y)
        if abs(delta_x) > bat_speed and abs(delta_x) > bat_speed:
            enemy_move_x = random.random() < 0.5
        if enemy_move_x:
            self.rect.centerx += min(delta_x, bat_speed) if delta_x > 0 else max(delta_x, -bat_speed)
        else:
            self.rect.centery += min(delta_y, bat_speed) if delta_y > 0 else max(delta_y, -bat_speed)

    #
    # def draw(self):
    #     self.image = bat_sprites_R[0]
    #     self.screen.blit(self.image, self.rect)


class Bat_boss(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Bat_boss, self).__init__()
        self.screen = screen
        self.image = bat_boss_sprites_R[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice([random.randint(1281, 1300), random.randint(1159, 1279) - 1280])
        self.rect.centery = random.choice([random.randint(721, 760), random.randint(619, 719) - 720])
        self.health = 1000
        self.damage = 1
        self.exp = 100
        self.rank = 'common'

    @property
    def pos(self):
        return float(self.rect.centerx), float(self.rect.centery)

    def update(self, player, anim_count_bat):
        if self.rect.centerx > player.rect.centerx:
            self.image = bat_boss_sprites_R[int(anim_count_bat // 10)]
        else:
            self.image = bat_boss_sprites_L[int(anim_count_bat // 10)]
        delta_x = player.rect.centerx - self.rect.centerx
        delta_y = player.rect.centery - self.rect.centery
        enemy_move_x = abs(delta_x) > abs(delta_y)
        if abs(delta_x) > bat_speed and abs(delta_x) > bat_speed:
            enemy_move_x = random.random() < 0.5
        if enemy_move_x:
            self.rect.centerx += min(delta_x, bat_speed) if delta_x > 0 else max(delta_x, -bat_speed)
        else:
            self.rect.centery += min(delta_y, bat_speed) if delta_y > 0 else max(delta_y, -bat_speed)

from math import *
import pygame

#game settings
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILE = 10


#player settings
player_pos = (WIDTH//2, HEIGHT//2)
player_angle = 0
player_speed = 2
player_sprites_R = [pygame.image.load(f'img/whiper_{i}_R.png') for i in range(4)]
player_sprites_L = [pygame.image.load(f'img/whiper_{i}_L.png') for i in range(4)]



#colors
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)

#bat settings
bat_speed = 1.5
bat_sprites_R = [pygame.image.load(f'img/bat_{i}_R.png') for i in range(2)]
bat_sprites_L = [pygame.image.load(f'img/bat_{i}_L.png') for i in range(2)]
bat_boss_sprites_R = [pygame.image.load(f'img/bat_boss_{i}_R.png') for i in range(2)]
bat_boss_sprites_L = [pygame.image.load(f'img/bat_boss_{i}_L.png') for i in range(2)]

#attack_sprites
attack_sprites_R = pygame.image.load(f'img/anim_whip_4_R.png')
attack_sprites_L = pygame.image.load(f'img/anim_whip_4_L.png')
garlic_spite = pygame.image.load('img/Garlic.png')
garlic_spite.set_alpha(90)



from math import *
import pygame

#game settings
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILE = 10
lvl_background = pygame.image.load('img/lvl_background.png')
menu_background = pygame.image.load('img/BG.png')
button_background = pygame.image.load('img/Button_background.png')
button_background_red = pygame.image.load('img/Button_background_red.png')

#player settings
player_pos = (WIDTH//2, HEIGHT//2)
player_angle = 0
player_speed = 2
player_sprites_R = [pygame.image.load(f'img/whiper_{i}_R.png') for i in range(4)]
player_sprites_L = [pygame.image.load(f'img/whiper_{i}_L.png') for i in range(4)]

#player_stats
player_health_multiplier = [1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2]
player_speed_multiplier = [1, 1.1, 1.2, 1.3, 1.5, 1.7, 2]
whip_damage_multiplier = [1, 1.5, 2.4, 2.7, 3, 3.3, 3.7]
whip_scale_multiplier = [1, 1, 1.3, 1.3, 1.7, 1.7, 2]
garlic_damage_multiplier = [1, 1.5, 1.9, 2.3, 2.5, 2.7, 3]
garlic_scale_multiplier = [[1, 1, 1.2, 1.2, 1.4, 1.4, 1.5]]


#colors
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
SEA_GREEN = (46, 139, 87)
DarkSlateBlue = (72, 61, 139)
DarkGoldenRod = (184, 134, 11)

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

#items_sprites
crystals = [pygame.image.load(f'img/crystal_lvl_{i}.png') for i in range(1, 6)]
couns = [pygame.image.load(f'img/gold_coin.png'), pygame.image.load(f'img/coin_bag.png'),
         pygame.image.load(f'img/rich_coin_bag.png')]
floor_chicken = pygame.image.load(f'img/floor_chicken.png')
garlic_icon = pygame.image.load(f'img/garlic_icon.png')
magic_wand_icon = pygame.image.load(f'img/magic_wand_icon.png')
whip_icon = pygame.image.load(f'img/whip_icon.png')
fire_wand_icon = pygame.image.load(f'img/fire_wand_icon.png')
chest = pygame.image.load(f'img/chest.png')



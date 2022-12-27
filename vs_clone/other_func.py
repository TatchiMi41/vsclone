import pygame
from weapon import *
from enemy import *
from player import *
from settings import *



def collide_weapon_and_enemy(player, enemy, weapon, mob_exp):
    for i in enemy:
        if pygame.sprite.collide_rect(weapon, i):
            if i.rect.centerx > player.rect.centerx:
                if weapon == Whip:
                    i.rect.centerx += 15
                i.health -= weapon.damage
            else:
                if weapon == Whip:
                    i.rect.centerx -= 35
                i.health -= weapon.damage
            if i.rect.centery > player.rect.centery:
                if weapon == Whip:
                    i.rect.centery += 15
                i.health -= weapon.damage
            else:
                if weapon == Whip:
                    i.rect.centery -= 15
                i.health -= weapon.damage
        if i.health <= 0:
            player.kill_count_exp += mob_exp
            i.kill()

def collide_enemy_and_player(player, enemy):
    for i in enemy:
        if pygame.sprite.collide_rect(player, i):
            player.health -= i.damage

def check_events(screen, whip_delay, weapon_group, player, weapon):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == whip_delay and player.alive():
            weapon_group.add(weapon)
            weapon_group.update(player)
            weapon_group.draw(screen)
            weapon.kill()

def print_text(screen, massage, x, y, font_color=(0, 0, 0), font_type='timesnewromanpsmt.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(massage, True, font_color)
    screen.blit(text, (x, y))

def check_alive(player, bats, bats_boss, screen, player_group, whip_group):
    if player.health <= 0:
        player.kill()
        bats.empty()
        whip_group.empty()
        bats_boss.empty()
        print_text(screen, 'please press the SPACEBAR to start over', 640, 360)
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            player_group.add(player)
            player.health = 100



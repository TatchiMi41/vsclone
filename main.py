import pygame
from dataclasses import dataclass

from other_func import *
from items import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('vsc')
clock = pygame.time.Clock()
game = False
menu = True
ad_menu = False

anim_count_bat = 0
anim_count_player = 0
anim_count_whip = 0
anim_count_garlic = 0

player = Player(screen)
player_group = pygame.sprite.Group()
player_group.add(player)
whip_group = pygame.sprite.Group()
whip = Whip(screen, player)
garlic = Garlic(screen, player)
whip_group.add(whip)
drop_group = pygame.sprite.Group()

bats = pygame.sprite.Group()
bats_boss = pygame.sprite.Group()

damage_to_player_event = pygame.USEREVENT
pygame.time.set_timer(damage_to_player_event, 100)

background = pygame.image.load('img\\background.png')
background_rect = background.get_rect()

scroll = [0, 0]


def menu_game_switch():
    global menu, game
    if menu:
        game = True
        menu = False
    elif game:
        game = False
        menu = True


def show_game():
    global anim_count_bat, anim_count_whip, anim_count_player, anim_count_garlic
    check_events()


    # screen.blit(background, (background_rect.x - scroll[0], background_rect.y - scroll[1]))
    screen.blit(background, background_rect)
    player_group.draw(screen)
    player_group.update(anim_count_player)
    draw_hp_bar(screen, player)

    whip_group.draw(screen)
    whip_group.update(player, anim_count_whip)
    # pygame.draw.line(screen, GREEN, player.pos,
    #                  (player.rect.centerx + WIDTH * math.cos(player.angle), player.rect.centery))

    if len(bats) < 10:
        bat = Bat(screen)
        bats.add(bat)

    if len(bats_boss) < 1:
        bat_boss = Bat_boss(screen)
        bats_boss.add(bat_boss)

    anim_count_bat += 1
    if anim_count_bat == 20:
        anim_count_bat = 0

    anim_count_player += 1
    if anim_count_player == 40:
        anim_count_player = 0

    anim_count_whip += 1
    if anim_count_whip == 100:
        anim_count_whip = 0

    anim_count_garlic += 1
    if anim_count_garlic == 100:
        anim_count_garlic = 0

    bats.update(player, anim_count_bat)
    bats.draw(screen)
    bats_boss.update(player, anim_count_bat)
    bats_boss.draw(screen)

    collide_weapon_and_enemy(player, bats, whip, screen, drop_group)
    collide_enemy_and_player(player, bats)
    collide_weapon_and_enemy(player, bats_boss, whip, screen, drop_group)
    collide_enemy_and_player(player, bats_boss)

    collide_drop(player, drop_group)
    drop_group.draw(screen)

    if player.lvl >= 10:
        garlic.activate = True

    if garlic.activate:
        garlic.update(player, anim_count_garlic)
        garlic.draw()
        # if garlic.image.get_alpha() == 90:
        collide_weapon_and_enemy(player, bats, garlic, screen, drop_group)
        collide_weapon_and_enemy(player, bats_boss, garlic, screen, drop_group)

    # if player.kill_count_exp >= player.exp:
    #     player.lvl += 1
    #     player.kill_count_exp = 0
    #     upgades_menu(screen)
    lvl_up(screen, player, bats, bats_boss, whip)

    check_alive(player, bats, bats_boss, screen, player_group, whip_group, drop_group, menu_game_switch, whip)

    game_UI(screen, player)

    pygame.display.flip()
    clock.tick(FPS)

def show_menu():
    start_button = Button(button_background, button_background)
    quit_button = Button(button_background_red, button_background_red)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(menu_background, (0, 0))
    screen.blit(pygame.image.load('img/title.png'), (500, 50))
    start_button.draw(screen, 525, 275, 'Начать', menu_game_switch)
    quit_button.draw(screen, 525, 375, 'Выйти', shift=(80, 10), action=exit)
    pygame.display.update()
    clock.tick(60)

def game_process():
    global game, menu

    game_process_cycle = True
    while game_process_cycle:
        if menu:
            show_menu()
        elif game:
            show_game()

game_process()
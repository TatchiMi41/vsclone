import random
import pygame

from other_func import *
from items import *

pygame.init()
time_after_init = pygame.time.get_ticks()
time_after_start_game = 0
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
anim_count_magic_bullet = 0

player = Player(screen)
player_group = pygame.sprite.Group()
player_group.add(player)
whip_group = pygame.sprite.Group()
whip = Whip(screen, player)
garlic = Garlic(screen, player)
whip_group.add(whip)
drop_group = pygame.sprite.Group()
other_weapon_group = pygame.sprite.Group()

bats = pygame.sprite.Group()
bats_boss = pygame.sprite.Group()
zombies = pygame.sprite.Group()

damage_to_player_event = pygame.USEREVENT
pygame.time.set_timer(damage_to_player_event, 100)

create_magic_bullet = pygame.USEREVENT + 1
pygame.time.set_timer(create_magic_bullet, 500)

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
    global anim_count_bat, anim_count_whip, anim_count_player, anim_count_garlic, anim_count_magic_bullet, magic_bullet, enemy, time_after_start_game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if time_after_start_game == 0:
        time_after_start_game = pygame.time.get_ticks()

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
    if len(zombies) < 20 and (time_after_init - time_after_start_game) > 60000:
        zombie = Zombie(screen)
        zombies.add(zombie)

    if len(bats_boss) < 1:
        bat_boss = Bat_boss(screen, player)
        bats_boss.add(bat_boss)

    if anim_count_magic_bullet == 0:
        enemy = random.choice(random.choices([bats, bats_boss])[0].sprites())
        magic_bullet = Magic_Wand(screen, player, enemy)
        if magic_bullet.activate:
            other_weapon_group.add(magic_bullet)
            other_weapon_group.update()

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

    anim_count_magic_bullet += 1
    if anim_count_magic_bullet == 300:
        anim_count_magic_bullet = 0

    bats.update(player, anim_count_bat)
    bats.draw(screen)
    bats_boss.update(player, anim_count_bat)
    bats_boss.draw(screen)
    zombies.update(player, anim_count_bat)
    zombies.draw(screen)

    other_weapon_group.draw(screen)
    other_weapon_group.update()
    for i in other_weapon_group:
        check_in_window(i)

    collide_weapon_and_enemy(player, bats, whip, screen, drop_group)
    collide_weapon_and_enemy(player, bats_boss, whip, screen, drop_group)
    collide_weapon_and_enemy(player, zombies, whip, screen, drop_group)
    for i in other_weapon_group:
        collide_weapon_and_enemy(player, bats, i, screen, drop_group)
        collide_weapon_and_enemy(player, bats_boss, i, screen, drop_group)
        collide_weapon_and_enemy(player, zombies, i, screen, drop_group)
    collide_enemy_and_player(player, bats)
    collide_enemy_and_player(player, bats_boss)
    collide_enemy_and_player(player, zombies)

    collide_drop(player, drop_group)
    drop_group.draw(screen)

    if garlic.activate:
        garlic.update(player, anim_count_garlic)
        garlic.draw()
        collide_weapon_and_enemy(player, bats, garlic, screen, drop_group)
        collide_weapon_and_enemy(player, bats_boss, garlic, screen, drop_group)
        collide_weapon_and_enemy(player, zombies, garlic, screen, drop_group)

    lvl_up(screen, player, bats, bats_boss, zombies, whip, magic_bullet, garlic)

    check_alive(player, bats, bats_boss, screen, player_group, whip_group, drop_group, menu_game_switch, whip, other_weapon_group)

    game_UI(screen, player)

    pygame.display.flip()
    clock.tick(FPS)

def show_menu():
    start_button = Button(button_background, button_background, 'start_button')
    quit_button = Button(button_background_red, button_background_red, 'start_button')

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
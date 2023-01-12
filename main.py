import pygame.time

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
other_weapon_group = pygame.sprite.Group()

bats = pygame.sprite.Group()
bats_boss = pygame.sprite.Group()
zombies = pygame.sprite.Group()

background = pygame.image.load('img\\background.png')
background_rect = background.get_rect()


def menu_game_switch():
    global menu, game
    if menu:
        game = True
        menu = False
    elif game:
        game = False
        menu = True


def show_game():
    global anim_count_bat, anim_count_whip, anim_count_player, anim_count_garlic, time_after_start_game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(background, background_rect)
    player_group.draw(screen)
    player_group.update(anim_count_player)
    draw_hp_bar(screen, player)

    whip_group.draw(screen)
    whip_group.update(player, anim_count_whip)

    if len(bats) < 10:
        bat = Bat(screen)
        bats.add(bat)

    if len(zombies) < (20 + ((pygame.time.get_ticks()//1000)//60) * 5) and pygame.time.get_ticks() > 120000:
        zombie = Zombie(screen)
        zombies.add(zombie)

    if len(bats_boss) < 1:
        bat_boss = Bat_boss(screen, player)
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

    lvl_up(screen, player, bats, bats_boss, zombies, whip, garlic)

    check_alive(player, bats, bats_boss, screen, player_group, whip_group, drop_group, menu_game_switch, whip,
                other_weapon_group)

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

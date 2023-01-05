import pygame

from other_func import *
from items import *


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('vsc')
clock = pygame.time.Clock()
# game = False
# menu = True

def game_cycle():
    global screen, clock
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

    whip_delay = pygame.USEREVENT + 1
    pygame.time.set_timer(whip_delay, whip.delay_to_attack)

    background = pygame.image.load('img\\background.png')
    background_rect = background.get_rect()


    running = True
    while running:


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
        check_events(screen, whip_delay, whip_group, player, whip)

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
            garlic.drawing()
            # if garlic.image.get_alpha() == 90:
            collide_weapon_and_enemy(player, bats, garlic, screen, drop_group)
            collide_weapon_and_enemy(player, bats_boss, garlic, screen, drop_group)

        if player.kill_count_exp >= player.exp:
            player.lvl += 1
            player.kill_count_exp = 0
        check_alive(player, bats, bats_boss, screen, player_group, whip_group, drop_group)

        game_UI(screen, player)

        pygame.display.flip()
        clock.tick(FPS)

# def game_process(screen, clock):
#     global game, menu
#
#     game_process_cycle = True
#     while game_process_cycle:
#         print(menu, game)
#         if menu == False:
#             game_cycle()
#         if menu:
#             show_menu(screen, clock)

show_menu(screen, clock, game_cycle)
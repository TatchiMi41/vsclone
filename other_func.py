import pygame
import random
from weapon import *
from enemy import *
from player import *
from settings import *
from items import *

update_menu_flag = True
new_upgrade_pool = []


class Button:
    def __init__(self, active_image, inactive_image, name):
        self.color = (160, 82, 45)
        self.active_image = active_image
        self.rect_active = self.active_image.get_rect()
        self.width = self.rect_active.width
        self.height = self.rect_active.height
        self.inactive_image = inactive_image
        self.rect_inacrive_image = inactive_image
        self.name = name

    def draw(self, screen, x, y, massage, action=None, font_size=50, shift=(75, 10), action2=None):
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < cursor[0] < x + self.width and y < cursor[1] < y + self.height:
            screen.blit(self.active_image, (x, y))

            if click[0]:
                if action is not None:
                    action()
                if action2 is not None:
                    action2()
        else:
            screen.blit(self.inactive_image, (x, y))

        print_text(screen, massage, x + shift[0], y + shift[1], font_size=font_size, font_color=WHITE)


def game_UI(screen, player):
    draw_lvl_bar(screen, player)
    screen.blit(pygame.transform.scale(lvl_background, (50, 50)), (1230, 0))
    if player.lvl < 10:
        print_text(screen, f'{player.lvl}', 1248, 8, font_size=30, font_color=SEA_GREEN)
    else:
        print_text(screen, f'{player.lvl}', 1241, 8, font_size=30, font_color=SEA_GREEN)


def collide_weapon_and_enemy(player, enemy, weapon, screen, drop_group):
    for i in enemy:
        if pygame.sprite.collide_rect(weapon, i):
            if i.rect.centerx > player.rect.centerx:
                if weapon.title == 'Whip':
                    i.rect.centerx += 15
                i.health -= weapon.damage
            else:
                if weapon.title == 'Whip':
                    i.rect.centerx -= 35
                i.health -= weapon.damage
            if i.rect.centery > player.rect.centery:
                if weapon.title == 'Whip':
                    i.rect.centery += 15
                i.health -= weapon.damage
            else:
                if weapon.title == 'Whip':
                    i.rect.centery -= 15
                i.health -= weapon.damage
        if i.health <= 0:
            if i.rank == 'common':
                drop_group.add(Drop(screen, i.pos, i.exp, i.rank))
            else:
                drop_group.add(Drop(screen, i.pos, i.exp, i.rank))
            player.kills += 1
            i.kill()


def collide_drop(player, drops):
    for i in drops:
        if pygame.sprite.collide_rect(player, i):
            if i.type == 'crystal':
                player.kill_count_exp += i.exp
                i.kill()
            elif i.type == 'chest':

                i.kill()


def collide_enemy_and_player(player, enemy):
    for i in enemy:
        if pygame.sprite.collide_rect(player, i):
            player.health -= i.damage


def check_in_window(weapon):
    if weapon.rect.left > WIDTH or weapon.rect.right < 0 or weapon.rect.bottom < 0 or weapon.rect.top > HEIGHT:
        weapon.kill()


def print_text(screen, massage, x, y, font_color=(0, 0, 0), font_type='timesnewromanpsmt.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(massage, True, font_color)
    screen.blit(text, (x, y))


def check_alive(player, bats, bats_boss, screen, player_group, whip_group, drop_group, game_switch, whip,
                other_weapon_group, zombies, garlic):
    if player.health <= 0:
        after_death_menu(screen, player)
        player.kill()
        bats.empty()
        zombies.empty()
        whip_group.empty()
        bats_boss.empty()
        drop_group.empty()
        other_weapon_group.empty()
        garlic.activate = False


        def restart_game():
            nonlocal player, player_group, whip
            player_group.add(player)
            whip_group.add(whip)
            player.health = 100
            player.lvl = 1
            player.kill_count_exp = 0
            player.kills = 0
            player.rect.x = WIDTH // 2
            player.rect.y = HEIGHT // 2

        back_to_menu_button = Button(button_background_red, button_background_red, 'back_to_menu_button')
        back_to_menu_button.draw(screen, 507, 561, 'Вернуться в меню', shift=(32, 25), font_size=30, action=game_switch,
                                 action2=restart_game)
        restart_button = Button(button_background, button_background, 'restart_button')
        restart_button.draw(screen, 507, 461, 'Начать заново', shift=(55, 23), font_size=30, action=restart_game)


def draw_hp_bar(screen, player):
    hp_bar_height = 5
    hp_bar_width = 38
    hp_count = [100, 120, 140, 160, 180, 200, 220]
    fill = 100
    for i in range(7):
        if player.health_lvl == i:
            fill = (player.health / hp_count[i]) * hp_bar_width

    outline_rect = pygame.Rect(player.pos[0] - 3, player.pos[1] + 37, hp_bar_width, hp_bar_height)
    fill_rect = pygame.Rect(player.pos[0] - 3, player.pos[1] + 37, fill, hp_bar_height)
    pygame.draw.rect(screen, RED, fill_rect)
    pygame.draw.rect(screen, BLACK, outline_rect, 1)


def draw_lvl_bar(screen, player):
    lvl_bar_height = 20
    lvl_bar_width = WIDTH
    fill = (player.kill_count_exp / player.exp) * lvl_bar_width
    outline_rect = pygame.image.load(f'img/lvlbar.png')
    fill_rect = pygame.Rect(0, 0, fill, lvl_bar_height)
    pygame.draw.rect(screen, SEA_GREEN, fill_rect)
    screen.blit(outline_rect, (0, 0))


def after_death_menu(screen, player, ):
    results_box_fill = pygame.Rect(350, 50, 600, 600)
    results_box_outline = pygame.Rect(350, 50, 600, 600)
    pygame.draw.rect(screen, DarkSlateBlue, results_box_fill)
    pygame.draw.rect(screen, DarkGoldenRod, results_box_outline, 2)
    print_text(screen, 'Результаты', 586, 84, font_color=WHITE)
    print_text(screen, f'Убито врагов:  {player.kills}', 357, 140, font_color=WHITE)
    print_text(screen, f'Уровень:   {player.lvl}', 357, 166, font_color=WHITE)


def lvl_up(screen, player, bats, bats_boss, zombies, whip, garlic):
    if player.kill_count_exp >= player.exp:
        upgrades_menu(screen, bats, bats_boss, zombies, player, whip, garlic)


def upgrades_menu(screen, bats, bats_boss, zombies, player, whip, garlic):
    global update_menu_flag, new_upgrade_pool

    def upgrade_hp():
        global update_menu_flag
        nonlocal player
        if player.health_lvl < 7:
            player.health_lvl += 1
            player.update_upgrades(player_health_multiplier, 'health')
            player.lvl += 1
            player.kill_count_exp = 0
            for bat in bats:
                bat.speed = bat_speed
            for bat in bats_boss:
                bat.speed = bat_speed
            for bat in zombies:
                bat.speed = bat_speed
        update_menu_flag = True

    def upgrade_speed():
        global update_menu_flag
        nonlocal player
        if player.speed_lvl < 7:
            player.speed_lvl += 1
            player.update_upgrades(player_speed_multiplier, 'speed')
            player.lvl += 1
            player.kill_count_exp = 0
            for bat in bats:
                bat.speed = bat_speed
            for bat in bats_boss:
                bat.speed = bat_speed
            for bat in zombies:
                bat.speed = bat_speed
        update_menu_flag = True

    def upgrade_whip():
        global update_menu_flag
        nonlocal whip
        if whip.lvl < 7:
            whip.lvl += 1
            whip.update_upgrades(whip_damage_multiplier, 'damage')
            whip.update_upgrades(whip_scale_multiplier, 'scale')
            player.lvl += 1
            player.kill_count_exp = 0
            for bat in bats:
                bat.speed = bat_speed
            for bat in bats_boss:
                bat.speed = bat_speed
            for bat in zombies:
                bat.speed = bat_speed
        update_menu_flag = True

    def max_upgrades():
        global update_menu_flag
        player.lvl += 1
        player.kill_count_exp = 0
        for bat in bats:
            bat.speed = bat_speed
        for bat in bats_boss:
            bat.speed = bat_speed
        for bat in zombies:
            bat.speed = bat_speed
        update_menu_flag = True

    def upgrade_garlic():
        global update_menu_flag
        nonlocal garlic
        if garlic.lvl < 7:
            garlic.lvl += 1
            garlic.activate = True
            player.lvl += 1
            player.kill_count_exp = 0
            for bat in bats:
                bat.speed = bat_speed
            for bat in bats_boss:
                bat.speed = bat_speed
            for bat in zombies:
                bat.speed = bat_speed
        update_menu_flag = True

    for i in bats:
        i.speed = 0
    for i in bats_boss:
        i.speed = 0
    for i in zombies:
        i.speed = 0
    results_box_fill = pygame.Rect(350, 50, 600, 600)
    results_box_outline = pygame.Rect(350, 50, 600, 600)
    pygame.draw.rect(screen, DarkSlateBlue, results_box_fill)
    pygame.draw.rect(screen, DarkGoldenRod, results_box_outline, 2)
    print_text(screen, 'Выберите улучшение', 586, 84, font_color=WHITE)

    # create all buttons
    speed_upgrade_button = Button(speed_upgrade_button_img, speed_upgrade_button_img, 'speed_upgrade_button')
    hp_upgrade_button = Button(hp_upgrade_button_img, hp_upgrade_button_img, 'hp_upgrade_button')
    whip_upgrade_button = Button(whip_upgrade_button_img, whip_upgrade_button_img, 'whip_upgrade_button')
    garlic_upgrade_button = Button(garlic_upgrade_button_img, garlic_upgrade_button_img, 'garlic_upgrade_button')
    upgrade_pool = [speed_upgrade_button, hp_upgrade_button, whip_upgrade_button, garlic_upgrade_button]

    if garlic.activate is True:
        upgrade_pool.remove(garlic_upgrade_button)
    if whip.lvl >= 6:
        upgrade_pool.remove(whip_upgrade_button)
    if player.speed_lvl >= 6:
        upgrade_pool.remove(speed_upgrade_button)
    if player.health_lvl >= 6:
        upgrade_pool.remove(hp_upgrade_button)
    if player.health_lvl >= 6 and player.speed_lvl >= 6 and whip.lvl >= 6 and garlic.activate is True:
        update_menu_flag = False

    if update_menu_flag is True and len(upgrade_pool) > 2:
        new_upgrade_pool = random.sample(upgrade_pool, k=3)
        update_menu_flag = False
    elif update_menu_flag is True and (len(upgrade_pool) == 2):
        new_upgrade_pool = random.sample(upgrade_pool, k=2)
        update_menu_flag = False
    elif update_menu_flag is True and (len(upgrade_pool) == 1):
        new_upgrade_pool = upgrade_pool

    if upgrade_pool:
        if len(new_upgrade_pool) == 3:
            for i in range(3):
                if i == 0:
                    if new_upgrade_pool[i].name == 'speed_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 140, massage=None, action=upgrade_speed, font_size=30)
                    elif new_upgrade_pool[i].name == 'hp_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 140, massage=None, action=upgrade_hp, font_size=30)
                    elif new_upgrade_pool[i].name == 'whip_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 140, massage=None, action=upgrade_whip, font_size=30)
                    elif new_upgrade_pool[i].name == 'garlic_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 140, massage=None, action=upgrade_garlic, font_size=30)
                elif i == 1:
                    if new_upgrade_pool[i].name == 'speed_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 280, massage=None, action=upgrade_speed, font_size=30)
                    elif new_upgrade_pool[i].name == 'hp_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 280, massage=None, action=upgrade_hp, font_size=30)
                    elif new_upgrade_pool[i].name == 'whip_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 280, massage=None, action=upgrade_whip, font_size=30)
                    elif new_upgrade_pool[i].name == 'garlic_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 280, massage=None, action=upgrade_garlic, font_size=30)
                elif i == 2:
                    if new_upgrade_pool[i].name == 'speed_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 420, massage=None, action=upgrade_speed, font_size=30)
                    elif new_upgrade_pool[i].name == 'hp_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 420, massage=None, action=upgrade_hp, font_size=30)
                    elif new_upgrade_pool[i].name == 'whip_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 420, massage=None, action=upgrade_whip, font_size=30)
                    elif new_upgrade_pool[i].name == 'garlic_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 420, massage=None, action=upgrade_garlic, font_size=30)
        elif len(new_upgrade_pool) == 2:
            for i in range(2):
                if i == 0:
                    if new_upgrade_pool[i].name == 'speed_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 140, massage=None, action=upgrade_speed, font_size=30)
                    elif new_upgrade_pool[i].name == 'hp_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 140, massage=None, action=upgrade_hp, font_size=30)
                    elif new_upgrade_pool[i].name == 'whip_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 140, massage=None, action=upgrade_whip, font_size=30)
                    elif new_upgrade_pool[i].name == 'garlic_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 140, massage=None, action=upgrade_garlic, font_size=30)
                elif i == 1:
                    if new_upgrade_pool[i].name == 'speed_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 280, massage=None, action=upgrade_speed, font_size=30)
                    elif new_upgrade_pool[i].name == 'hp_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 280, massage=None, action=upgrade_hp, font_size=30)
                    elif new_upgrade_pool[i].name == 'whip_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 280, massage=None, action=upgrade_whip, font_size=30)
                    elif new_upgrade_pool[i].name == 'garlic_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 280, massage=None, action=upgrade_garlic, font_size=30)
        elif len(new_upgrade_pool) == 1:
            for i in range(1):
                if i == 0:
                    if new_upgrade_pool[i].name == 'speed_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 140, massage=None, action=upgrade_speed, font_size=30)
                    elif new_upgrade_pool[i].name == 'hp_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 140, massage=None, action=upgrade_hp, font_size=30)
                    elif new_upgrade_pool[i].name == 'whip_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 140, massage=None, action=upgrade_whip, font_size=30)
                    elif new_upgrade_pool[i].name == 'garlic_upgrade_button':
                        new_upgrade_pool[i].draw(screen, 352, 140, massage=None, action=upgrade_garlic, font_size=30)
    else:
        return_to_game = Button(button_background, button_background, 'return_to_game_button')
        return_to_game.draw(screen, 507, 461, 'Продолжить без улучшений', shift=(45, 23), font_size=20,
                            action=max_upgrades)
        print_text(screen, 'Максимальное количество улучшений', 372, 280, font_color=WHITE)

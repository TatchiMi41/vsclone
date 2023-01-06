import pygame
from weapon import *
from enemy import *
from player import *
from settings import *
from items import *

class Button:
    def __init__(self, active_image, inactive_image):
        self.color = (160, 82, 45)
        self.active_image = active_image
        self.rect_active = self.active_image.get_rect()
        self.width = self.rect_active.width
        self.height = self.rect_active.height
        self.inactive_image = inactive_image
        self.rect_inacrive_image = inactive_image

    def draw(self, screen, x, y, massage, action=None, font_size=50, shift=(75, 10)):
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < cursor[0] < x + self.width and y < cursor[1] < y + self.height:
            screen.blit(self.active_image, (x, y))

            if click[0]:
                if action is not None:
                    action()
        else:
            screen.blit(self.inactive_image, (x, y))

        print_text(screen, massage, x + shift[0], y + shift[1], font_size=font_size, font_color=WHITE)


def game_UI(screen, player):
    draw_lvl_bar(screen, player)
    screen.blit(pygame.transform.scale(lvl_background, (50, 50)), (1230, 0))
    print_text(screen, f'{player.lvl}', 1248, 8, font_size=30, font_color=SEA_GREEN)


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
            drop_group.add(Drop(screen, i.pos, i.exp, i.rank))
            player.kills += 1
            # if player.health_lvl != 6:
            #     player.health_lvl += 1
            #     player.update_upgrades(player_health_multiplier)
            #     print(player.health_lvl, player.health)
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


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


def print_text(screen, massage, x, y, font_color=(0, 0, 0), font_type='timesnewromanpsmt.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(massage, True, font_color)
    screen.blit(text, (x, y))


def check_alive(player, bats, bats_boss, screen, player_group, whip_group, drop_group):
    if player.health <= 0:
        after_death_menu(screen, player)
        player.kill()
        bats.empty()
        whip_group.empty()
        bats_boss.empty()
        drop_group.empty()

        def restart_game():
            nonlocal player, player_group
            player_group.add(player)
            player.health = 100
            player.lvl = 1
            player.kill_count_exp = 0
            player.kills = 0

        restart_button = Button(button_background, button_background)
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
    outline_rect = pygame.Rect(0, 0, lvl_bar_width, lvl_bar_height)
    fill_rect = pygame.Rect(0, 0, fill, lvl_bar_height)
    pygame.draw.rect(screen, SEA_GREEN, fill_rect)
    pygame.draw.rect(screen, BLACK, outline_rect, 2)


def after_death_menu(screen, player):
    results_box_fill = pygame.Rect(350, 50, 600, 600)
    results_box_outline = pygame.Rect(350, 50, 600, 600)
    pygame.draw.rect(screen, DarkSlateBlue, results_box_fill)
    pygame.draw.rect(screen, DarkGoldenRod, results_box_outline, 2)
    print_text(screen, 'Результаты', 586, 84, font_color=WHITE)
    print_text(screen, f'Убито врагов:  {player.kills}', 357, 140, font_color=WHITE)
    print_text(screen, f'Уровень:   {player.lvl}', 357, 166, font_color=WHITE)
    print_text(screen, f'Заработано золота:   ', 357, 195, font_color=WHITE)
    back_to_menu_button = Button(button_background_red, button_background_red)
    back_to_menu_button.draw(screen, 507, 561, 'Вернуться в меню', shift=(32, 25), font_size=30)


def lvl_up(screen, player):
    if player.kill_count_exp >= player.exp:
        upgades_menu(screen)

        # player.lvl += 1
        # player.kill_count_exp = 0


def upgades_menu(screen):
    results_box_fill = pygame.Rect(350, 50, 600, 600)
    results_box_outline = pygame.Rect(350, 50, 600, 600)
    pygame.draw.rect(screen, DarkSlateBlue, results_box_fill)
    pygame.draw.rect(screen, DarkGoldenRod, results_box_outline, 2)
    print_text(screen, 'Выберите улучшение', 586, 84, font_color=WHITE)
    speed_update_button = Button(speed_upgrade_button_img, speed_upgrade_button_img)
    speed_update_button.draw(screen, 537, 140, 'Увеличивает скорость бега на 10%')
    hp_upgrade_button = Button(hp_upgrade_button_img, hp_upgrade_button_img)
    hp_upgrade_button.draw(screen, 537, 340, 'Увеличиват количество хп на 20%')

from other_func import *
from UI import *

anim_count_bat = 0
anim_count_player = 0


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('vsc')
clock = pygame.time.Clock()

player = Player(screen)
player_group = pygame.sprite.Group()
player_group.add(player)
whip_group = pygame.sprite.Group()
whip = Whip(screen, player)
garlic = Garlic(screen, player)
# whip_group.add(whip)

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

    bats.update(player, anim_count_bat)
    bats.draw(screen)
    bats_boss.update(player, anim_count_bat)
    bats_boss.draw(screen)
    check_events(screen, whip_delay, whip_group, player, whip)

    collide_weapon_and_enemy(player, bats, whip, 10)
    collide_enemy_and_player(player, bats)
    collide_weapon_and_enemy(player, bats_boss, whip, 100)
    collide_enemy_and_player(player, bats_boss)

    if player.lvl >= 10:
        garlic.activate = True

    if garlic.activate:
        garlic.update(player)
        garlic.drawing()
        collide_weapon_and_enemy(player, bats, garlic, 10)
        collide_weapon_and_enemy(player, bats_boss, garlic, 100)

    if player.kill_count_exp >= player.exp:
        player.lvl += 1
        player.kill_count_exp = 0

    check_alive(player, bats, bats_boss, screen, player_group, whip_group)

    print_text(screen, f'lvl={player.lvl}', 0, 0)
    print_text(screen, f'{player.health}', 0, 680, (139, 0, 0))





    pygame.display.flip()
    clock.tick(FPS)

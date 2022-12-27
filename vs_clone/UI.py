import pygame
from settings import *
from other_func import *


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = (160, 82, 45)

    def draw(self, screen, x, y, massage, action=None, font_size=30):
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < cursor[0] < x + self.width and y < cursor[1] < y + self.height:
            pygame.draw.rect(screen, self.color, (x, y, self.width, self.height))

            if click[0] and action is not None:
                action()

        print_text(screen, massage, x + 10, y + 10, font_size=font_size)

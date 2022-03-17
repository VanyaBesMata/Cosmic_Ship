import pygame
import control
from Cosmic_ship import Ship
from pygame.sprite import Group


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("First game")
    bg_color = (0, 0, 0)
    ship = Ship(screen)
    bullets = Group()
    ufos = Group()
    control.create_units(screen, ufos)


    while True:
        control.event(screen, ship, bullets)
        ship.update_ship()
        control.update(bg_color, screen, ship, bullets)
        control.update_bullets(bullets)

run_game()
import pygame
import sys
from bullet import Bullet
from enemy import UFO


def event(screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.mright = True
            elif event.key == pygame.K_LEFT:
                ship.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, ship)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.mright = False
            elif event.key == pygame.K_LEFT:
                ship.mleft = False


def update(bg_color, screen, ship, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bul()
    ship.draw_ship()
    #ufos.draw_enemy(screen)
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_units(screen, ufos):
    ufo = UFO(screen)
    ufo_width = ufo.rect.width
    all_ufo_x = int((700 - 2 * ufo_width) / ufo_width)

    for ufo_one in range(all_ufo_x):
        ufo = UFO(screen)
        ufo.x = ufo_width + ufo_width * ufo_one
        ufo.rect.x = ufo.x
        ufo.add(ufos)



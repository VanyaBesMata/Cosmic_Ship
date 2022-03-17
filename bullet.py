import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(1, 1, 6, 10)
        self.color = 240, 98, 145
        self.speed = 3.5
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bul(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


import pygame


class UFO(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(UFO, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/pixil-frame-1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_enemy(self):
        self.screen.blit(self.image, self.rect)



import pygame


class Ship:
    """A spaceship control class"""
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('/home/aleksei/projects/alien_invasion'
                                       '/alien_invasion/images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class representing a single alien"""
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        self.image = pygame.image.load('/home/aleksei/projects/alien_invasion'
                                       '/alien_invasion/images/alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

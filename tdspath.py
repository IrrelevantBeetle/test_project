import pygame, math, random, sys

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,  0, 255)


class Path (pygame.sprite.Sprite):
    def __init__ (self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.image.fill ((0, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.arrow = pygame.Surface((100, 80), pygame.SRCALPHA)
        
        pygame.draw.line(self.image, GREEN ,[0,0], [0,100], 2)
        pygame.draw.line(self.image, GREEN ,[0,80], [80,100], 2)
        pygame.draw.line(self.arrow, WHITE, [15,50], [100,50], 2)
        pygame.draw.line(self.arrow, WHITE, [62.5,80], [100,50], 2)
        pygame.draw.line(self.arrow, WHITE, [62.5,20], [100,50], 2)
        self.image.blit(self.arrow, (0,0))

    def update (self, move):
        self.image.fill(BLACK)
        pygame.draw.line(self.image, GREEN ,[0,0], [100,0], 2)
        pygame.draw.line(self.image, GREEN ,[0,98], [100,98], 2)
        self.image.blit(self.arrow, (move,0))
        self.image.blit(self.arrow, (move - 100,0))
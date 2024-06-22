import pygame

class ScoreZone:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.passed = False

    def update(self, speed):
        self.rect.x -= speed

    def draw(self, screen):
        pass

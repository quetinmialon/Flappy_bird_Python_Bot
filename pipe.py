import pygame
import random
from score_zone import ScoreZone

PIPE_WIDTH = 52
PIPE_HEIGHT = 320
GAP_SIZE = 150
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PIPE_SPACING = 200  # Espacement constant entre les paires de tuyaux

class Pipe:
    def __init__(self, x):
        original_image = pygame.image.load('pipe.png')
        self.image_bottom = pygame.transform.scale(original_image, (PIPE_WIDTH, PIPE_HEIGHT))
        self.image_top = pygame.transform.flip(self.image_bottom, False, True)
        self.rect_top = self.image_top.get_rect()
        self.rect_bottom = self.image_bottom.get_rect()
        self.rect_top.x = x
        self.rect_bottom.x = x
        self.reset()
        self.score_zone = ScoreZone(self.rect_top.x + PIPE_WIDTH, self.rect_top.y + PIPE_HEIGHT, PIPE_WIDTH, GAP_SIZE)

    def reset(self):
        self.rect_top.y = random.randint(-PIPE_HEIGHT + 50, 0)
        self.rect_bottom.y = self.rect_top.y + PIPE_HEIGHT + GAP_SIZE
        self.score_zone = ScoreZone(self.rect_top.x + PIPE_WIDTH, self.rect_top.y + PIPE_HEIGHT, PIPE_WIDTH, GAP_SIZE)

    def update(self):
        self.rect_top.x -= 3
        self.rect_bottom.x -= 3
        self.score_zone.update(3)
        if self.rect_top.x < -PIPE_SPACING:
            self.rect_top.x = SCREEN_WIDTH
            self.rect_bottom.x = SCREEN_WIDTH
            self.reset()

    def draw(self, screen):
        screen.blit(self.image_top, self.rect_top)
        if self.rect_top.y + PIPE_HEIGHT < 0:
            top_extension_rect = pygame.Rect(self.rect_top.x, self.rect_top.y + PIPE_HEIGHT, PIPE_WIDTH, -self.rect_top.y)
            screen.fill((0, 255, 0), top_extension_rect)
        
        screen.blit(self.image_bottom, self.rect_bottom)
        if self.rect_bottom.y + PIPE_HEIGHT < SCREEN_HEIGHT:
            bottom_extension_rect = pygame.Rect(self.rect_bottom.x, self.rect_bottom.y + PIPE_HEIGHT, PIPE_WIDTH, SCREEN_HEIGHT - (self.rect_bottom.y + PIPE_HEIGHT))
            screen.fill((0, 255, 0), bottom_extension_rect)

        self.score_zone.draw(screen)

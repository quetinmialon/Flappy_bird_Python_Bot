import pygame

GRAVITY = 0.5
FLAP_STRENGTH = -10

class Bird:
    def __init__(self):
        original_image = pygame.image.load('bird.png')
        self.image = pygame.transform.scale(original_image, (34, 24)) 
        self.rect = self.image.get_rect()
        self.rect.center = (100, 300)
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += int(self.velocity)

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)

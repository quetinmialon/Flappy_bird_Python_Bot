import pygame
from bird import Bird
from pipe import Pipe

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PIPE_SPACING = 200 
PIPE_WIDTH = 52

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()
        self.bird = Bird()
        self.pipes = []
        self.init_pipes()
        self.running = True
        self.font = pygame.font.SysFont('gothica', 20)
        self.score = 0

    def init_pipes(self):
        for i in range(SCREEN_WIDTH//PIPE_SPACING + 1):
            self.pipes.append(Pipe(SCREEN_WIDTH + i * PIPE_SPACING))

    def check_collision(self):
        for pipe in self.pipes:
            if self.bird.rect.colliderect(pipe.rect_top) or self.bird.rect.colliderect(pipe.rect_bottom):
                return True
        if self.bird.rect.top <= 0 or self.bird.rect.bottom >= SCREEN_HEIGHT:
            return True
        return False

    def check_score_zone(self):
        for pipe in self.pipes:
            if pipe.score_zone.rect.colliderect(self.bird.rect) and not pipe.score_zone.passed:
                self.score += 1
                pipe.score_zone.passed = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.bird.flap()

            self.bird.update()

            for pipe in self.pipes:
                pipe.update()

            if self.check_collision():
                self.running = False

            self.check_score_zone()

            self.screen.fill((135, 206, 235))
            self.bird.draw(self.screen)
            for pipe in self.pipes:
                pipe.draw(self.screen)

            score_text = self.font.render(f'score : {self.score}', 1, (250, 250, 250))
            self.screen.blit(score_text, (20, 20))

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

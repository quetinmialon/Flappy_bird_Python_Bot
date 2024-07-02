import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pygame
from bird import Bird
from pipe import Pipe
from skimage import color, transform

class FlappyBirdEnv(gym.Env):
    def __init__(self):
        super(FlappyBirdEnv, self).__init__()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.bird = Bird()
        self.pipes = []
        self.init_pipes()
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(
            low=0, high=255, shape=(84, 84, 1), dtype=np.uint8
        )

    def init_pipes(self):
        for i in range(800 // 200 + 1):
            self.pipes.append(Pipe(800 + i * 200))

    def reset(self, **kwargs):
        self.bird = Bird()
        self.pipes = []
        self.init_pipes()
        self.score = 0
        return self._get_state()

    def step(self, action):
        if action == 1:
            self.bird.flap()
        self.bird.update()
        for pipe in self.pipes:
            pipe.update()
        reward = 1
        done = self._is_done()
        if done:
            reward = -100
        self._check_score_zone()
        state = self._get_state()
        return state, reward, done, {}

    def render(self, mode='human'):
        self.screen.fill((135, 206, 235))
        self.bird.draw(self.screen)
        for pipe in self.pipes:
            pipe.draw(self.screen)
        score_text = pygame.font.SysFont('gothica', 20).render(f'score : {self.score}', 1, (250, 250, 250))
        self.screen.blit(score_text, (20, 20))
        pygame.display.flip()
        self.clock.tick(30)

    def _get_state(self):
        state = pygame.surfarray.array3d(self.screen)
        state = color.rgb2gray(state)  # Convert to grayscale
        state = transform.resize(state, (84, 84))  # Resize to 84x84
        state = np.expand_dims(state, axis=-1)  # Ajouter une dimension pour le canal unique
        state = (state * 255).astype(np.uint8)  # Convertir à uint8
        return state

    def _is_done(self):
        if self.bird.rect.top <= 0 or self.bird.rect.bottom >= 600:
            return True
        for pipe in self.pipes:
            if self.bird.rect.colliderect(pipe.rect_top) or self.bird.rect.colliderect(pipe.rect_bottom):
                return True
        return False

    def _check_score_zone(self):
        for pipe in self.pipes:
            if pipe.score_zone.rect.colliderect(self.bird.rect) and not pipe.score_zone.passed:
                self.score += 1
                pipe.score_zone.passed = True

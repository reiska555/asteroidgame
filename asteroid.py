import random
import pygame
from logger import log_event
from circleshape import LINE_WIDTH, CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return "this was a small asteroid and we're done"
        else:
            log_event("asteroid_split")
            split_angle = random.uniform(20, 50)
            a_1_velocity = self.velocity.rotate(split_angle)
            a_2_velocity = self.velocity.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_1.velocity = a_1_velocity * 1.2
            asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_2.velocity = a_2_velocity * 1.2

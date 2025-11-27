from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import pygame
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        old_radius = self.radius
        #old_velocity = self.velocity
        #old_position = self.position
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        velocity_one = self.velocity.rotate(angle)
        velocity_two = self.velocity.rotate(angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = velocity_one * 1.2
        asteroid_two.velocity = velocity_two * 1.2


    
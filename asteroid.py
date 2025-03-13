from circleshape import *
import pygame
import random
import pygame.math
from  constants import *


class Asteroid(CircleShape):
     def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
       

     def draw(self, screen):
        pygame.draw.circle(screen, ("palegreen3"), self.position, self.radius, 2)

    
     def update(self, dt):
        self.position += self.velocity * dt
   
     def split(self):
         random_angle = random.uniform(20,30)
         self.velocity.rotate
         self.kill()

        # If the asteroid is too small to split, just return
         if self.radius <= ASTEROID_MIN_RADIUS:
            return
   
         else:
            angle = random.uniform(20, 50)
            A1 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS ))
            A2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS ))
            A1.velocity = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
            A2.velocity = pygame.math.Vector2.rotate(self.velocity, -angle) * 1.2

        

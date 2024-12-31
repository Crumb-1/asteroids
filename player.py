from circleshape import *
from constants import *

class Player(CircleShape):
    #constructor inputs
    def __init__(self,x: int ,y: int):
        #call parent class constructoe 
        super().__init__(x, y, PLAYER_RADIUS)
        #set rotation
        self.rotation = 0

    #triangle 
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    
    
    def draw(self, screen):
        # Draw the player as a polygon
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


        
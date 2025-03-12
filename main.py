import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
from circleshape import *
from Shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

   
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # Instantiate the Player at the center of the screen
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update objects in updatable group
        for obj in updatable:
            obj.update(dt)

        # Fill screen with black
        screen.fill("black")

        # Draw objects in drawable group
        for obj in drawable:
            obj.draw(screen)
       
        #update display
        pygame.display.flip()

         # Collision detection between player and asteroids
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                exit("Game Over!")
            
                return

        # Refresh screen with each iteration
        dt = clock.tick(60) / 1000
    


if __name__ == "__main__":
    main()
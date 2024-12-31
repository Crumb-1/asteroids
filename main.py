import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Instantiate the Player at the center of the screen
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    running = True
    while running:
        dt = clock.tick(60) / 1000  # Get delta time (seconds)

        # Handle events (e.g., closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update player position based on input
        player.update(dt)

        # Fill screen with black
        screen.fill((0, 0, 0))

        # Draw player
        player.draw(screen)

        # Refresh screen with each iteration
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
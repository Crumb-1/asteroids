import pygame
from constants import *
from player import *
def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Instantiate the Player at the center of the screen
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    #stop program if window closed 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    #infinite loop to keep program alive
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #fill screen with black 
        screen.fill((0,0,0))

        #draw player
        player.draw(screen)

        #refresh screen with each iterartion
        pygame.display.flip()

        #limit fps to 60 & get delta time
        Clock.tick(60)
        dt = Clock.get_time() / 1000

    
    return dt
if __name__ == "__main__":
    main()
    
import pygame
from constants import *

def main():
    #init state
    pygame.init()
    #init FPS boundaries / time
    MAX_FRAME_RATE = 60
    CLOCK = pygame.time.Clock()
    STABILIZE_FPS = CLOCK.tick(MAX_FRAME_RATE) / 1000
    #delta time variable
    DT = 0
    #set and define screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #start game loop
    while True:
        #create and enable quit function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #fill screen
        pygame.Surface.fill(screen, (0,0,0))
        #flip screen
        pygame.display.flip()
        DT = STABILIZE_FPS
        
if __name__ == "__main__":
    main()
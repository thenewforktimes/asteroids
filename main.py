import pygame
from constants import *

def main():
    #init state
    pygame.init()
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
           
if __name__ == "__main__":
    main()
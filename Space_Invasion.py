#import modules
import sys
import pygame

#main function for running game
def run_game():
    #init game and create object
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")


    #Start main loop for game
    while True:

        #Watch for keyboard andmouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Make most recently drawn screen visible
        pygame.display.flip()

run_game()



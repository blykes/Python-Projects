#import modules
import sys
import pygame

from settings import settings

#main function for running game
def run_game():
    #init game and create object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screenwidth, ai_settings.screenheight))
    pygame.display.set_caption("Alien Invasion")

    #set color
    bg_color = (230, 230, 230)
    

    #Start main loop for game
    while True:

        #Watch for keyboard andmouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Redraw scree with each pass through the loop
            screen.fill.(ai_settings.bg_color)
            

        #Make most recently drawn screen visible
        pygame.display.flip()

run_game()



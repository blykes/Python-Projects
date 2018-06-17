#import modules
#import sys removed as no longer needed in main file. Imported via game_functions
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship

#main function for running game
def run_game():
    #init game and create object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invasion")

    #set color
    bg_color = (230, 230, 230)
    
    #Make a ship
    ship = Ship(ai_settings, screen)
    

    #Start main loop for game
    while True:
    	gf.check_events(ship)
    	gf.update.screen(ai_settings, screen, ship)

run_game()



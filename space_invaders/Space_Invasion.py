#import modules

import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

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
    
    # Make a group to store bullets
    bullets = Group()

    #Make a group of aliens
    aliens = Group()

    #Creates Alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Start main loop for game
    while True:
    	gf.check_events(ai_settings, screen, ship, bullets)
    	ship.update()
    	gf.update_bullets(bullets)
    	gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()

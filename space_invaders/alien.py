#Modul imports
import pygame
from pygame.sprite import Sprite

#Class for Alien fleet
class Alien(Sprite):
	
	#Create Alien and set start position
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien at top of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store exact position of alien
        self.x = float(self.rect.x)
     
    #Checks if alien is at edge of screen and returns True if it is   
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    #Move alien either direction   
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x
	#Draw alien at current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)

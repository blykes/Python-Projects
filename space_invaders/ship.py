#Modules
import pygame
from pygame.sprite import Sprite

#Creates ship and starting location
class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Loads ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Starts each new ship at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #Stores local decimal value for ship center
        self.center = float(self.rect.centerx)
        
        #Movement
        self.moving_right = False
        self.moving_left = False
	
	#Center ship    
    def center_ship(self):
        self.center = self.screen_rect.centerx
    
    #Update ship based on movement 
    def update(self):
    
        #Update ship's center value but not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        #Update rect object from self.center
        self.rect.centerx = self.center
	
	#Draw ship at current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)

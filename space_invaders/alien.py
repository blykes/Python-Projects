import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
# Class represents alien fleet 

    def __init__(self, ai_settings, screen):
    #initialize the alien and set starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load tha alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Starts each alien at the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact psotion
        self.x = float(self.rect.x)
        
    def check_edges (self):
    #return true if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True
            
    def update(self):
        #move alien right or left 
        self.x += (self.ai_settings.alien_speed_factor *
                      self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        #Draw Alien at current location
        self.screen.blit(self.image, self.rect)
        

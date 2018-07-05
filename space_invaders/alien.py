import pygame
from pyagme.sprite import Sprite

# Class represents alien fleet 
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        #self.ai_settings = ai_settings

        #Load tha alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image_rect()

        #Starts each alien at the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact psotion
        self.x = float(self.rect.x)

    def blitme(self):
        #Draw Alien at current location
        self.screen.blit(self.image, self.rect)
        

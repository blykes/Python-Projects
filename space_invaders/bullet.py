#Imports
import pygame
from pygame.sprite import Sprite

#Class manages bullets fired from ship
class Bullet(Sprite):
	#Creates bulet at current position of ship
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        #Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #Stores position of bullet in decimal value 
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
	
	#Moves bullet up screen
    def update(self):
        #Update decimal position of bullet
        self.y -= self.speed_factor
        
        #Update  rect position
        self.rect.y = self.y
	
	#Draw Bullet
    def draw_bullet(self):
       
        pygame.draw.rect(self.screen, self.color, self.rect)

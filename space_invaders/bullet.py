import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	# This is the class that manages bullets fired form the ship 
	def __init__(self, ai_settings, scree, ship):
	
	# create bullet object st ships current position
	super().__init__()
	self.screen = screen
	
	#Create bullet rect at (0,0) andn then set the correct position
	self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
	self.rect.acenterx = self .rect.centerx
	self.rect.top = ship.rect.top
	
	# Store the bullet's position as a decimal value
	self.y = float (self.rect.y)
	
	self.color = ai_settings.bullet.color
	self.speed_factor - ai_settings.bullet_speed_factor 
	
	def update(self):
	# Move the bullet up the screen
	# update the decimal position of the bullet 
	self.y -= self.speed_factor
	
	# update the rect position
	self.rect.y = self.y
	
	def draw_bullet(self):
	# Draw the bullet on screen
	pygame.draw.rect(sef.screen, self.color, self.rect)
	
import sys
import pygame


def check_events(ship):
	#Respond to keypresses and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT():
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if even.key == pygameK_RIGHT:
			# Moves ship right
			ship.react.centerx +=1 
			
def update_screen(ai_settings, screen, ship):
	"""" Updates images on screen and flips to new screen
	# Redraw screen during each pass of loop """"
	screen.fill(ai_settings.bg_color)
            ship.blitme()
	# Make most recently drawn screen visible
        pygame.display.flip()
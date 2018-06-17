import sys
import pygame

# Respond to key press events
def check_keydown_events(event, ship)
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
		
# Respond to key release events 
def check_keyup_events(event, ship)
	
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship. moving_left = False
		
# Respond to keypresses and mouse events
def check_events(ship):
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship)
		
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			# Moves ship right
				ship.rect.centerx += 1 
			
def update_screen(ai_settings, screen, ship):
        
	# Updates images on screen and flips to new screen
	screen.fill(ai_settings.bg_color)
	ship.blitme()

	# Make most recently drawn screen visible
	pygame.display.flip()
	

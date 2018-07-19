import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien

#Keypress events are here
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

#Keyrelease events are here        
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

#Keypress and mouse events
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)

#Starts new game when play button is clicked
def check_play_button(stats, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
    
# Create new bullet, add it to group, and fire if limit not yet reached            
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

#Update images on screen
def update_screen(ai_settings, screen, ship, aliens, bullets, play_button):
    # Redraw the screen, each pass through the loop
    screen.fill(ai_settings.bg_color)
    
    #Redraw all bullets, behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #Draw play button while game is inactive
    if not stats.game_active:
        play_button.draw_button()
        

    #Make the most recently drawn screen visible
    pygame.display.flip()

#update bullets and remove old ones    
def update_bullets(ai_settings, screen, ship, aliens, bullets):
    #Update bullet positions
    bullets.update()

    #Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

#Responds to alien bullet colliosions. Removes any bullet/alien collisions          
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if len(aliens) == 0:
        #Destroy existing bullets and create new fleet
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

#Check for edges and respond appropriately     
def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
#Drop the fleet one level and change direction        
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
#Respond to aliens hitting ship    
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        #Decrement ships_left
        stats.ships_left -= 1
    else:
        stats.game_active = False
    
    #Empty lists of aliens and bullets
    aliens.empty()
    bullets.empty()
    
    #Create a new fleet and recenter ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    
    #Pause
    sleep(0.5)

##Check if aliens have reached bottom of screen
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

#Check for edge and update position of all aliens            
def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    #Check for alien/ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    #Check for aliens hitting bottom
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
#Determines number of aliens in a row            
def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

#Determines number of rows    
def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

#Create and alien and place in row    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
#Create A fleet of aliens
def create_fleet(ai_settings, screen, ship, aliens):
    """Creates an alien to find the number of aliens in a row
    with spacing equal to one alien width"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)
    
    #Create the fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)

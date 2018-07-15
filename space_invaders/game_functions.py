import sys
import pygame


from bullet import Bullet

#Respond to key press events
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

#Create new bullet and add it to group
#Create a new bullet and fire if limit not yet reached
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

# Respond to key release events 
def check_keyup_events(event, ship):
    #Response to key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
		
# Respond to keypresses and mouse events
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
#Update position of bullets and and remove old ones
def update_bullets(aliens, bullets):
    #Update bullet positions.
    bullets.update()
    
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #Check for bullets that have hit aliens
    #Get rid of both bullet and alien
    collisions = pygame.sprite.groupcollide(bullets, a;iens, True, True)

    #destroy existing bullets and create new fleet
    if len(aliens) ==0:
        bullets.empty()
        createfleet(ai_settings, screen, ship, aliens)
    

    #check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def change_fleet_direction(ai_settings, aliens):
    #drop the fleet and cheange direction
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
        
def check_fleet_edges(ai_settings, aliens):
    #checks for edges and responds appropriately
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
    
def update_screen(ai_settings, screen, ship, aliens, bullets):
    #Updates images on the screen and flip to new screen
    #Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #alien.blitme()
    #Make the most recently drawn screen visible.
    pygame.display.flip()

def update_aliens(ai_settings, aliens):
    #check for edge and update the position of all aliens in fleet
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

def get_number_aliens_x(ai_settings, alien_width):
    #determines number of aliens that fit in a row
    available_space_x = ai_settings.screen.width - 2 * alien_width #margin
    number_aliens_x = int(avalilable_space_x / (2*alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    #find the fumber of alien rows that will fit on screen
    available_space_y = (ai_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number):
    #create an aliens and place it in row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    
def create_fleet(ai_settings, screen, ship, aliens):
    #create a fleet of aliens
    #creates an alien to find the number of aliens in a row
    #spacing equal to one alien width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)
 
    #create the fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)

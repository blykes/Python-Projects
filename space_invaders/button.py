import pygame.font

class Button():
    #Init button attributes
    def __init__ (self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #Set dimensions and properties of button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Build button's object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #Prep button message once
        self.prep_msg(msg)
        
        
        

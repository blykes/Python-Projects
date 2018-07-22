#Class contains all settings for Space Invasion game
class Settings():
	
	#Start game's settings
    def __init__(self):
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        #Ship settings
        self.ship_limit = 3
            
        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        #Alien settings
        self.fleet_drop_speed = 10
            
        #Adjusts rate of game speed as game progresses
        self.speedup_scale = 1.1
        
        #RAte of point value increase as game progresses
        self.score_scale = 1.5
    
        self.initialize_dynamic_settings()
	
	#Start dynamic settings that can change as game progresses
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        #Scoring
        self.alien_points = 50
    
        #Fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
    
    #Increases speed and point values as level increases
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)

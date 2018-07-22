#Class tracks stats for game
class GameStats():
    #Begins stats
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        #Start game in inactive state
        self.game_active = False
        
        #High score. Should not reset
        self.high_score = 0
    
    #Initialize stats that do change during play    
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

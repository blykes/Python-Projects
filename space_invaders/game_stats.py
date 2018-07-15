class GameStats()
    #This class tracks the stats for the game

    def __init__(self, ai_settings):
        #Initializes statistics
        self.ai_settingsd = ai_settings
        self.reset_stats()

    def reset_stats(self):
        #Initialze stats that can change during gameplay
        self.ships_left = self.ai_settings.ship_limit
        

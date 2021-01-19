import pygame


class Scoreboard:
    """ class for score reporting """
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.screen_rect= self.screen.get_rect()
        self.settings=ai_game.settings
        self.stats= ai_game.stats

        #setting of scoring table
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)

        #prepare initiale score format
        self.prep_score()
        self.prep_high_score()


    def prep_score(self):
        """ score become rendered image """
        score_str= str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right -20
        self.score_rect.top=self.screen_rect.top + 40

    def prep_high_score(self):
        """ score become rendered image """
        high_score_str= str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)

        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.high_score_rect.top 
         
    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
        
    def show_score(self):
    # Draw blank button and then draw message.
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
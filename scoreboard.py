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


    def prep_score(self):
        """ score become rendered image """
        score_str= str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right -20
        self.score_rect.top=self.screen_rect.top + 40


    def show_score(self):
    # Draw blank button and then draw message.
        self.screen.blit(self.score_image, self.score_rect)
from ship import Ship
from settings import Settings
import sys
import pygame






class Alien_invasion:
    """class to manage the game"""

    def __init__(self):
        """initialise the game and create game ressources"""
        pygame.init()
        self.settings=Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
        
        pygame.display.set_caption("Alien invasion")
        self.ship=Ship(self)

    def run_game(self):
        """start the game by calling a main loop"""
        while True:
             # wait keyboard or mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # draw the screen after all the changes occured
            
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()
if __name__=="__main__":
    partie = Alien_invasion()
    partie.run_game()

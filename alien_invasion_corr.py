from ship import Ship
from settings import Settings
import sys
import pygame


class Alien_invasion:
    """class to manage the game"""

    def __init__(self):
        """initialise the game and create game ressources"""
        pygame.init()
        #print("ouzou")
        self.settings=Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
        
        pygame.display.set_caption("Alien invasion")
        self.ship = Ship(self)
        
    def run_game(self):
        """start the game by calling a main loop"""
        while True:
            print("izann")
             # wait keyboard or mouse event
            for event in pygame.event.get():      ###syntax
                if event.type == pygame.QUIT:     ###syntax
                    sys.exit()
           # draw the screen after all the changes occurred   ###the following should not in the pygame event get loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            print("izan")
            pygame.display.flip()
            print("izan ssin")

if __name__ == "__main__":       ###syntax wrong
    partie = Alien_invasion()
    partie.run_game()
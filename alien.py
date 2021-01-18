import pygame
from pygame.sprite import Sprite
class Alien(Sprite):

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #load the alien image 
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        
        # position of each new alien
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #store the x position of each alien
        self.x = float(self.rect.x)
    


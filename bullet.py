import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """a Class to manage bullets"""

    def __init__(self,ai_game):
        """initialise a bullet"""
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color
        #create a bullet rect in the left top corner with width and height defined
        self.rect= pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop= ai_game.ship.rect.midtop
        self.y=float(self.rect.y) # pixel position are integer, we have to deal with floats !!!!

    def update(self):
        """move the bullet"""
        #update decimal position of bullet
        self.y-=self.settings.bullet_speed
        #move the real position of bullet
        self.rect.y=self.y
    def draw_bullet(self):
        #draw the bullet in the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
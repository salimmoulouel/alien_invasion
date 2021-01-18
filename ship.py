import pygame


class Ship:
   """A class to manage the ship."""
   def __init__(self, ai_game):
      """Initialize the ship and set its starting position."""
      self.screen = ai_game.screen
      self.settings = ai_game.settings
      self.screen_rect = ai_game.screen.get_rect()
      # Load the ship image and get its rect.
      self.image = pygame.image.load('images/ship.bmp')
      self.rect = self.image.get_rect()
      

      # Start each new ship at the bottom center of the screen.
      self.rect.midbottom = self.screen_rect.midbottom
      # set movement variable to default values
      self.moving_right = False
      self.moving_left = False
      self.x= float(self.rect.x)
   def blitme(self):
      """Draw the ship at its current location."""
      self.screen.blit(self.image, self.rect)
   def update(self):
      """update the ship position based on flag moving_right"""
      
      if((self.moving_right==True) & (self.rect.right<self.screen_rect.right)):
         #update the float x value
         self.x += self.settings.ship_speed
         #update the float x value                  
      if((self.moving_left==True) & (self.rect.left>0)):
         self.x -= self.settings.ship_speed
      # assign the integer part of x to the x of rect object, rect.x cant be float (it's a pixel)
      self.rect.x=self.x
from alien import Alien
from ship import Ship
from settings import Settings
import sys
import pygame




from bullet import Bullet

class Alien_invasion:
    """class to manage the game"""

    def __init__(self):
        """initialise the game and create game ressources"""
        pygame.init()
        self.settings=Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width, self.settings.screen_height = self.screen.get_rect().width, self.screen.get_rect().height
        pygame.display.set_caption("Alien invasion")
        self.ship=Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()



    def _create_fleet(self):
        """create fleet of aliens"""
        # create alien prototype to get the left begin width 
        alien = Alien(self)
        alien_width, alien_height = alien.rect.width, alien.rect.height
        #we calculate the aliens surface
            # we release 1 alien width in the left and right of screen
        available_space_x = self.settings.screen_width - ( 2 * alien_width) # corriger 1 au lieu de 2
            # we let 1 alien_width in the right of each alien
        number_aliens_x = available_space_x // (2 * alien_width)
        
            # we release 1 alien height in the top and 2 alien height bottom and the ship height
        available_space_y = (self.settings.screen_height - \
                            (3 * alien_height) - self.ship.rect.height)
            # we count how many rows of aliens are drawable
        number_aliens_y = available_space_y // (2 * alien_height)
            
        #one row fleet creation
        for row_number in range(number_aliens_y):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)
        

        
    def _create_alien(self,alien_number,row_number):
        """ create an alien and place it in the row fleet"""
        alien = Alien(self)
        #set the left position of each alien in the screen
        alien_width, alien_height=alien.rect.width, alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.x=alien.x
        alien.rect.y=alien.y 
        self.aliens.add(alien)


        

    def _check_event(self):
        """allow us to check if event occur and respond"""
         # wait keyboard or mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self._check_key_down_event(event)
            self._check_key_up_event(event)
            
    
    def _check_key_down_event(self,event):
        """check if key down event occure and respond
            a helper function which allow us to refractor code
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right=True
            elif event.key == pygame.K_LEFT:    
                self.ship.moving_left=True
            elif event.key == pygame.K_SPACE:
                self.fire_bullet()
            elif event.key == pygame.K_q:    
                sys.exit()
            
    def _check_key_up_event(self,event):
        """check if key up event occure and respond
            a helper function which allow us to refractor code
        """
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right=False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left=False
    
    def fire_bullet(self):
        """create new bullet and add it to Sprite group"""
        if(len(self.bullets)<self.settings.bullet_allowed):
            self.bullets.add(Bullet(self))
    def _update_screen(self):
        """update the screen content and flip the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # we can make it more beautiful by adding image to bullet object and call the draw method of sprit group
        #self.bullets.draw(self.screen) 

        #draw the aliens
        self.aliens.draw(self.screen)
        # draw the screen after all the changes occured
        pygame.display.flip()

    def _update_bullets(self):
        """update the ullet position and deal with out of screen bullet"""
        #update bullet position
        self.bullets.update()
        # remove out of screen bullets
        for bullet in self.bullets.copy():
                if( bullet.rect.bottom<=0 ):
                   self.bullets.remove(bullet)
    def run_game(self):
        """start the game by calling a main loop"""
        while True:
            self._check_event()  
            self.ship.update() 
            self._update_bullets()
            self._update_screen()
            

if __name__=="__main__":
    partie = Alien_invasion()
    partie.run_game()

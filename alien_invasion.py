from button import Button
from game_stats import GameStats
from alien import Alien
from ship import Ship
from settings import Settings
import sys
import pygame

import time




from bullet import Bullet
i=0

class Alien_invasion:
    """class to manage the game"""

    def __init__(self):
        """initialise the game and create game ressources"""
        pygame.init()
        self.settings=Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width, self.settings.screen_height = self.screen.get_rect().width, self.screen.get_rect().height
        pygame.display.set_caption("Alien invasion")
        #store the game statistics
        self.stats=GameStats(self)
        self.ship=Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Make the Play button.
        self.play_button = Button(self, "Jouer")


        

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            self._check_key_down_event(event)
            self._check_key_up_event(event)
            
    def _check_play_button(self,mouse_pos):
        """start game with click on play button"""
        # we check if the game is not activate and if the mouse pressed in the button position
        if (self.play_button.rect.collidepoint(mouse_pos)) & (not self.stats.game_active):
            self.stats.game_active=True
            self.stats.reset_stats()
            
            #empty the screen 
            self.aliens.empty()
            #draw new aliens and ship
            self._create_fleet()
            self.ship.center_ship()

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
        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        
        pygame.display.flip()

    def _update_bullets(self):
        """update the ullet position and deal with out of screen bullet"""
        #update bullet position
        self.bullets.update()
        # remove out of screen bullets
        for bullet in self.bullets.copy():
                if( bullet.rect.bottom<=0 ):
                   self.bullets.remove(bullet)
        
        # checks for colision between objects and remove them
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)

        #check if the fleet is empty (renew the fleet and destory all the bullet )
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            
    
    def _ship_hit(self):
        """ deal with the collision with ship """
        if(self.stats.ship_left>1):# we take 1 in place of zero to have ship limit and not ship_limit + 1
            self.stats.ship_left -= 1
            
            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()


            time.sleep(0.5)
        else:
            self.stats.game_active=False
    def _update_aliens(self):
        """ update position of all aliens"""
        self._check_fleet_edges()
        # for alien in self.aliens:
        #     alien.update()
        self.aliens.update()
        #if there is collision between aliens and the ship
        if ( pygame.sprite.spritecollideany(self.ship,self.aliens) ):
            self._ship_hit()

        self._check_aliens_bottom()
    def _check_aliens_bottom(self):
        screen_rect=self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break



    def _check_fleet_edges(self):
        """respond if any alien reached edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        """drop the entire fleet and change fleet direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

        

    def run_game(self):
        """start the game by calling a main loop"""
        while True:
            self._check_event()  
            if(self.stats.game_active):
                self.ship.update() 
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            

if __name__=="__main__":
    partie = Alien_invasion()
    partie.run_game()

import pygame 
from pygame.sprite import Group
from shipFile import Ship
import game_function as gf
from settings import Settings

def run_game():
    pygame.init()
    ai_setting = Settings()

    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    
    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()
    # simple stats placeholder
    stats = type('S', (), {})()
    # attach aliens group to settings so game_function can draw if needed
    ai_setting.aliens = aliens

    # create the fleet
    gf.create_fleet(ai_setting, screen, ship, aliens)
    running = True
    while running == True:        
        gf.check_event(ai_setting, screen, ship, bullets) 
        ship.update()
        bullets.update()
        # remove bullets that moved off the top of the screen
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        # update aliens and check collisions
        gf.update_aliens(ai_setting, screen, ship, aliens, bullets, stats)
        gf.check_bullet_alien_collisions(ai_setting, screen, ship, aliens, bullets, stats)

        gf.update_screen(ai_setting,screen,ship, bullets)

run_game()


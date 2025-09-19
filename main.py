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
    running = True
    while running == True:        
        gf.check_event(ai_setting, screen, ship, bullets) 
        ship.update()
        bullets.update()
        gf.update_screen(ai_setting,screen,ship, bullets)

run_game()


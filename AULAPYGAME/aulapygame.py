import pygame 
from settings import Settings
import sys
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heigth))
    pygame.display.set_caption("Alien invasion")
    ship = Ship(screen)
    screen.fill(ai_settings.bg_color)

    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen,ship)

run_game()
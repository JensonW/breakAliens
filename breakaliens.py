import sys

import pygame

from settings import Settings
from ship import Ship

def runGame():
    # pygame.init()
    # screen = pygame.display.set_mode((1200, 800))
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("break Aliens")

    # make a ship
    ship = Ship(screen)

    bg_color = (230, 230, 230)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()


runGame()

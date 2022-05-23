import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME

pygame.init()
surface = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Drop!")

while True:
    surface.fill((0,0,0))
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

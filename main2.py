import sys
import pygame 
from pygame.locals import *

# Global variable for the game 
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES={}
SCREEN = pygame.display.set_mode(SCREENWIDTH, SCREENHEIGHT)
PLAYER = 'A:\\Programming\\Python\\Flappy-Bird-\\pictures\\bird.png'
BACKGROUND = 'A:\\Programming\\Python\\Flappy-Bird-\\pictures\\background.png'
PIPE = '\n'

pygame.init()
def WelcomeScreen():

    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    basex = 0

    while(True):
        for event in pygame.event.get(): # exit of game (ESCAPE KEY TO QUIT)
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
            return

        else:
            pass
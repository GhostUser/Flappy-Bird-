import sys
import pygame 
from pygame.locals import *

# Global variable for the game 
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES={}
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
PLAYER = 'pictures\bird.png'
BACKGROUND = 'pictures\background.png'
PIPE = '\n'


def WelcomeScreen():

    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    basex = 0

    while(True):
        for event in pygame.event.get(): # exit of game (ESCAPE KEY TO QUIT)
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))  
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def Sprites():
    SCREEN.blit(GAME_SPRITES['background'], (0, 0))
    SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
    SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))

    pygame.display.update()
    FPSCLOCK.tick(FPS)

if __name__ == "__main__":

    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    GAME_SPRITES['base'] =pygame.image.load('pictures\base.png').convert_alpha()
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        WelcomeScreen()
        Sprites()
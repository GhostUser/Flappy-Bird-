import pygame
from pygame import event 
import sys


class Screen:
    NUM_BLOCKS_X = 9
    NUM_BLOCKS_Y = 17
    block_size = 30
    WIDTH, HEIGHT = block_size * NUM_BLOCKS_X, block_size * NUM_BLOCKS_Y
    FPS = 32
    window=pygame.display.set_mode((WIDTH,HEIGHT))
    bg=pygame.image.load('pictures\\background.png')
    bird=pygame.image.load('pictures\\bird.png')
    platorm=pygame.image.load('pictures\\base.png')


class Bird:
    Co_X=0
    Co_Y=0
    bird=pygame.image.load('pictures\\bird.png')

def bg_win():
    Screen.window.blit(Screen.bg, (0,0))
    Screen.window.blit(Screen.bird, (Screen.WIDTH//2, Screen.HEIGHT//2))
    Screen.window.blit(Screen.platorm, (0, 4*Screen.HEIGHT//5))
    pygame.display.update()


def Game_loop():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            sys.exit()

        keys=pygame.key.get_pressed()

        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            pass


def main():
    pygame.display.init()
    pygame.font.init()
    pygame.display.set_caption("Flappy Bird")
    pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
    bg_win()
    pygame.time.delay(50)
    run=True
    while run:
        Game_loop()

    pygame.quit()

if __name__=='__main__':
    main()







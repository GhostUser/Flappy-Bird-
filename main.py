import pygame
from pygame import event 
import sys



class Screen:
    NUM_BLOCKS_X = 16
    NUM_BLOCKS_Y = 20
    block_size = 30
    WIDTH, HEIGHT = block_size * NUM_BLOCKS_X, block_size * NUM_BLOCKS_Y
    FPS = 32



def Game_loop():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            sys.exit()

        keys=pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            pass


def main():
    pygame.display.init()
    pygame.font.init()
    pygame.display.set_caption("Flappy Bird")
    pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
    pygame.time.delay(50)
    run=True
    while run:
        Game_loop()

    pygame.quit()

if __name__=='__main__':
    main()







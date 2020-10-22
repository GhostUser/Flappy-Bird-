import pygame 

class Screen:
    NUM_BLOCKS_X = 40
    NUM_BLOCKS_Y = 30
    block_size = pygame.DEFAULT_RECT_SIZE
    WIDTH, HEIGHT = block_size * NUM_BLOCKS_X, block_size * NUM_BLOCKS_Y
    FPS = 32



def main():
    pygame.display.init()
    pygame.font.init()
    pygame.display.set_caption("Flappy Bird")
    pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))



if __name__=='main':
    main()







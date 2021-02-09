# _*_coding:utf-8_*_

import pygame
from pygame.locals import *
from sys import exit

def main():
    #初始化
    pygame.init()
    screen = pygame.display.set_mode((150, 100))
    pygame.display.set_caption("Test")

    #背景
    background = pygame.Surface(screen.get_size())
    backgroung = background.convert()
    background.fill((250, 250, 250))

    #文本
    font = pygame.font.Font(None, 36)
    text = font.render("Hello!", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)


    #blit
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #event
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:    #退出
                exit()
            elif event.type == KEYDOWN:    #还是退出
                if event.key == 27:
                    exit()
                

        screen.blit(background, (0, 0))
        pygame.display.flip()



if __name__ == '__main__':
    main()
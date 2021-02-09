# _*_coding:utf-8_*_

# 这个
# 是一个小练习吧...
# 作用是 可以将player对象显示在屏幕上
# (就这???)
# 显示部分做好了
# 接下来是移动操作


#加载模块
try:
    import pygame
    from pygame.locals import *
    from sys import exit
    import os
    import getopt
    import random
    import math
    from socket import *
except ImportError as err:
    print("无法加载模块... %s" % err )
    exit()

def load_png(name):
    '''加载图像并返回图像对象'''
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print("无法加载图片:", fullname)
        raise SystemExit(message)
    return image, image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)

        #加载一个图像
        self.image, self.rect = load_png(image_path)
        self.pos = (0, 0)
        
    #旋转
    def rotate(self):
        pygame.transform.rotate(self.image)

    #设置位置
    def set_pos(self, pos):
        self.pos = pos

    #根据位置计算drawpos
    def get_drawpos(self):
        return (self.pos[0] - self.rect.w / 2, self.pos[1] - self.rect.h / 2)

    #将对象blit在Surface上
    def blit_on(self, screen):
        screen.blit(self.image, self.get_drawpos())
        

#主程序
def main():
    #初始化
    pygame.init()
    screen_size = (720, 480)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Test")

    #背景
    background = pygame.Surface(screen.get_size())
    backgroung = background.convert()
    background.fill((233, 233, 233))

    #玩家
    player = Player("博丽灵梦.png")
    player.set_pos((100, 100))

    #blit
    screen.blit(background, (0, 0))
    player.blit_on(screen)
    pygame.display.flip()

    #主循环
    while True:
        #event
        for event in pygame.event.get():
            if event.type == QUIT:    #退出
                exit()
            elif event.type == KEYDOWN:    #还是退出
                if event.key == 27:
                    exit()

        #update
        screen.blit(background, (0, 0))
        player.blit_on(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()

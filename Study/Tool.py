# _*_coding:utf-8_*_

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

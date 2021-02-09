import pygame
from pygame.locals import *
from sys import exit
from random import randint

SCREEN_SIZE = (720, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []

while True:
    event = pygame.event.wait()
    event_text.append(str(event))

    event_text = event_text[int(-SCREEN_SIZE[1]/font_height):]

    if event.type == QUIT:
        exit()

    screen.fill((255, 255, 255))

    y = SCREEN_SIZE[1]-font_height

    for text in event_text:
        screen.blit(font.render(text, True, (randint(0, 255), randint(0, 255), randint(0, 255))), (0, y))
        y -= font_height

    pygame.display.update()

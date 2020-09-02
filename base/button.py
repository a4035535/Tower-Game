# -*- coding: utf-8 -*-
import pygame
from sys import exit
import sys
from pygame.locals import *



class Button(object):
    def __init__(self, upimage, downimage, position,screen,category):
        self.imageUp = pygame.transform.scale(pygame.image.load(upimage).convert_alpha(),(50,50))
        self.imageDown = pygame.transform.scale(pygame.image.load(downimage).convert_alpha(),(50,50))
        self.position = position
        self.screen=screen
        self.category=category



    def isOver(self):
        point_x, point_y = pygame.mouse.get_pos()
        x, y = self.position
        w, h = self.imageUp.get_size()

        in_x = x - w / 2 < point_x < x + w / 2
        in_y = y - h / 2 < point_y < y + h / 2
        if in_x and in_y:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    print(x,y)
                    # 获得鼠标位置
                    #mouse_image_filename="head"+str(x//60-1)+"0.jpg"
                    category=x//60-1
                    self.category=category
        return in_x and in_y

    def render(self):
        w, h = self.imageUp.get_size()
        x, y = self.position

        if self.isOver():
            self.screen.blit(self.imageDown, (x - w / 2, y - h / 2))
        else:
            self.screen.blit(self.imageUp, (x - w / 2, y - h / 2))

        return self.category



#游戏地图
import pygame
import sys
from pygame.locals import *


pygame.init()

map_w=1200
map_h=600
screen = pygame.display.set_mode((map_w,map_h))
pygame.display.set_caption("Drawing Rectangles")

bgcolor=0,200,0
color_base1 = 255,255,0
color_base2 = 255,0,0
width = 0 #solid fill
base_w=100
base_h=300
base_margin=(map_h - base_h)/2
pos_base1 = 0, base_margin, base_w, base_h
pos_base2 = map_w - base_w, base_margin, base_w, base_h

color_road=0,200,200
road_w=map_w - base_w*2
road_h=60
road_gap=(base_h - road_h*3)/3
road_margin=base_margin + road_gap/2
pos_road1=base_w,road_margin,road_w,road_h
pos_road2=base_w,road_margin + road_h + road_gap,road_w,road_h
pos_road3=base_w,road_margin + (road_h + road_gap)*2,road_w,road_h    

def Soldiers(crops):
    pass

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(bgcolor)
    pygame.draw.rect(screen, color_base1, pos_base1, width)
    pygame.draw.rect(screen, color_base2, pos_base2, width)
    pygame.draw.rect(screen, color_road, pos_road1, width)
    pygame.draw.rect(screen, color_road, pos_road2, width)
    pygame.draw.rect(screen, color_road, pos_road3, width)
    pygame.display.update()
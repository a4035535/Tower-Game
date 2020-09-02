# 游戏地图
import pygame
import sys

from button import Button
from pygame.locals import *

pygame.init()
from PIL import Image, ImageGrab
import warnings

warnings.filterwarnings("ignore")

map_w = 1200
map_h = 600
bgcolor = 0, 200, 0
color_base1 = 255, 255, 0
color_base2 = 255, 0, 0
width = 0  # solid fill
base_w = 100
base_h = 300
screen = pygame.display.set_mode((map_w, map_h))
pygame.display.set_caption("Drawing Rectangles")
background = pygame.image.load("map.jpg")
background = pygame.transform.scale(background, (1200, 600))
road = pygame.image.load("road.jpg")
# print(pygame.image.info())
road = pygame.transform.scale(road, (1200, 100))
category = -1
# photo = pygame.transform.scale(photo,(60,60))
base_left = pygame.image.load("base_left.png")
base_left = pygame.transform.scale(base_left, (base_w + 50, base_h + 100))
base_right = pygame.image.load("base_right.png")
base_right = pygame.transform.scale(base_right, (base_w + 50, base_h + 100))
base_margin = (map_h - base_h) / 2 + 140
pos_base1 = 0, base_margin - 100, base_w, base_h
pos_base2 = map_w - base_w - 50, base_margin - 100, base_w, base_h
color_road = 0, 200, 200
road_w = map_w - base_w * 2
road_h = 60
road_gap = (base_h - road_h * 3) / 3

road_margin = base_margin + road_gap / 2

pos_road1 = 0, road_margin, road_w, road_h
pos_road2 = 0, road_margin + road_h + road_gap, road_w, road_h
pos_road3 = 0, road_margin + (road_h + road_gap) * 2, road_w, road_h


class Soldier:
    def __init__(self, unit):
        self.pos = unit.pos
        self.arms = unit.ID
        self.state = unit.status


def mouse_move(mouse_image_filename):
    mouse_cursor = pygame.image.load(mouse_image_filename)
    mouse_cursor = pygame.transform.scale(mouse_cursor, (50, 50))
    x, y = pygame.mouse.get_pos()
    # 计算光标左上角位置
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    # 将光标画上去
    screen.blit(mouse_cursor, (x, y))


pos1 = base_w, road_margin, 60, 60
pos2 = base_w, road_margin + road_h + road_gap, 60, 60
pos3 = base_w, road_margin + (road_h + road_gap) * 2, 60, 60

s1 = Soldier(pos1, 2, 1)
s2 = Soldier(pos2, 3, 6)
s3 = Soldier(pos3, 4, 7)

road_index = 0
army = [s1, s2, s3]


class map:
    def __init__(self, army):
        self.category = category
        self.road_index = road_index
        self.army = army

    def Soldiers(self, army):

        for i in army:
            photo = pygame.image.load("move" + str(i.arms) + ".png")
            fight = pygame.image.load("fight" + str(i.arms) + ".png")
            move_wh = Image.open("move" + str(i.arms) + ".png").size
            fight_wh = Image.open("fight" + str(i.arms) + ".png").size
            if i.state < 4:
                screen.blit(photo, i.pos,
                            pygame.Rect((move_wh[0] / 4) * i.state, move_wh[1] / 2, move_wh[0] / 4, move_wh[1] / 4))
                i.state = (i.state + 1) % 4
            else:
                screen.blit(fight, i.pos,
                            pygame.Rect((fight_wh[0] / 4) * (i.state - 4), fight_wh[1] / 2, fight_wh[0] / 4,
                                        fight_wh[1] / 4))
                i.state = 4 + (i.state + 1) % 4

    def addSoldier(self, road_index, category):
        self.category = category
        self.road_index = road_index


    def getAttribute(self):
        return self.road_index,self.category

    def isOnclick(self):
        global category
        point_x, point_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                in_y0 = road_margin < point_y < road_margin + road_h
                in_y1 = road_margin + road_h + road_gap < point_y < road_margin + road_h + road_gap + road_h
                in_y2 = road_margin + (road_h + road_gap) * 2 < point_y < road_margin + (road_h + road_gap) * 2 + road_h
                print(point_y)
                if (in_y0):
                    # 加一个兵
                    self.addSoldier(0, category)
                    category = -1
                elif (in_y1):
                    # 加一个兵
                    self.addSoldier(1, category)
                    category = -1
                elif (in_y2):
                    # 加一个兵
                    self.addSoldier(2, category)
                    category = -1


if __name__ == "__main__":
    while True:
        game = map(army)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # screen.fill(bgcolor)
        screen.blit(background, (0, 0))
        screen.blit(road, pos_road1)
        screen.blit(road, pos_road2)
        screen.blit(road, pos_road3)

        screen.blit(base_left, pos_base1)
        screen.blit(base_right, pos_base2)
        # pygame.draw.rect(screen, color_base1, pos_base1, width)
        # pygame.draw.rect(screen, color_base2, pos_base2, width)
        # pygame.draw.rect(screen, color_road, pos_road1, width)
        # pygame.draw.rect(screen, color_road, pos_road2, width)
        # pygame.draw.rect(screen, color_road, pos_road3, width)
        game.Soldiers(army)
        # pygame.draw.rect(screen, color_army, (100,100,100,100), 0)
        for i in range(5):
            upImageFilename = "head" + str(i) + "0.jpg"
            downImageFilename = "head" + str(i) + "1.jpg"
            button = Button(upImageFilename, downImageFilename, (60 * (i + 1), 50), screen, category)
            category = button.render()
        if (category >= 0):
            mouse_image_filename = "head" + str(category) + "0.jpg"
            mouse_move(mouse_image_filename)
            game.isOnclick()

        pygame.display.update()

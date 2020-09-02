# 游戏地图
import pygame
import sys

from 实习.button import Button
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

#
# class Soldier:
#     def __init__(self, unit):
#         self.pos = unit.pos
#         self.arms = unit.ID
#         self.state = unit.status


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

road_index = 0


class map:
    def __init__(self, army, model):
        self.category = category
        self.road_index = road_index
        self.army = army
        self.model = model

    def Soldiers(self, army):

        for i in army:
            photo = pygame.image.load("move" + str(i.ID) + ".png")
            fight = pygame.image.load("fight" + str(i.ID) + ".png")
            move_wh = Image.open("move" + str(i.ID) + ".png").size
            fight_wh = Image.open("fight" + str(i.ID) + ".png").size
            if(i.flag=="right"):
                move_wh[1]/=2
                fight_wh[1]/=2
            if i.status < 4:
                screen.blit(photo, i.pos,
                            pygame.Rect((move_wh[0] / 4) * i.status, move_wh[1] / 2, move_wh[0] / 4, move_wh[1] / 4))
                #i.status = (i.status + 1) % 4
            else:
                screen.blit(fight, i.pos,
                            pygame.Rect((fight_wh[0] / 4) * (i.status - 4), fight_wh[1] / 2, fight_wh[0] / 4,
                                        fight_wh[1] / 4))
                #i.status = 4 + (i.status + 1) % 4

    def addSoldier(self, road_index, category):
        self.category = category
        self.road_index = road_index

    def getAttribute(self):
        return self.road_index, self.category

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
                row, id = game.getAttribute()
                print("row,id", row, id)
                self.model.add_unit(id, row, 'left')
                print(self.model.unit_list)
        # return self.model


if __name__ == "__main__":
    from 实习.battle_filed import battle_filed

    model = battle_filed()
    while True:
        # print(model.action())
        game = map(model.action(), model)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background, (0, 0))
        screen.blit(road, pos_road1)
        screen.blit(road, pos_road2)
        screen.blit(road, pos_road3)
        screen.blit(base_left, pos_base1)
        screen.blit(base_right, pos_base2)
        unit_lists,now_cd,max_cd=model.action()
        print(now_cd,max_cd)
        game.Soldiers(unit_lists)
        for i in range(5):
            upImageFilename = "head" + str(i) + "0.jpg"
            downImageFilename = "head" + str(i) + "1.jpg"
            button = Button(upImageFilename, downImageFilename, (60 * (i + 1), 50), screen, category)
            cd1 = pygame.draw.rect(screen,(0,255,0),(60*(i+1)+25, 25,6,50),0)
            if(max_cd[i]-now_cd[i]):
                cd2 = pygame.draw.rect(screen,(255,0,0),(60*(i+1)+25, 25,6,50*((max_cd[i]-now_cd[i])/max_cd[i])),0)



            category = button.render()
        if (category >= 0):
            mouse_image_filename = "head" + str(category) + "0.jpg"
            mouse_move(mouse_image_filename)
            game.isOnclick()
        pygame.display.update()

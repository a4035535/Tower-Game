# 游戏地图
import pygame
import sys
from battle_filed import battle_filed
from button import Button
from pygame.locals import *
from default_data import *

pygame.init()
from PIL import Image, ImageGrab
import warnings

warnings.filterwarnings("ignore")

map_w = 1200
map_h = 600
base_w = 100
base_h = 300
screen = pygame.display.set_mode((map_w, map_h))
pygame.display.set_caption("塔防")
background = pygame.image.load("map.jpg")
background = pygame.transform.scale(background, (1200, 600))
road = pygame.image.load("road.jpg")
left_win_img = pygame.image.load("win.png")
right_win_img = pygame.image.load("lose.png")
right_win_img = pygame.transform.scale(right_win_img, (531, 293))
road = pygame.transform.scale(road, (1200, 100))
category = -1

base_left = pygame.image.load("base_left.png")
base_left = pygame.transform.scale(base_left, (base_w + 50, base_h + 100))
base_right = pygame.image.load("base_right.png")
base_right = pygame.transform.scale(base_right, (base_w + 50, base_h + 100))
base_margin = (map_h - base_h) / 2 + 140
pos_base1 = 0, base_margin - 100, base_w, base_h
pos_base2 = map_w - base_w - 50, base_margin - 100, base_w, base_h
road_w = map_w - base_w * 2
road_h = 60
road_gap = (base_h - road_h * 3) / 3

road_margin = base_margin + road_gap / 2
pos_road1 = 0, road_margin, road_w, road_h
pos_road2 = 0, road_margin + road_h + road_gap, road_w, road_h
pos_road3 = 0, road_margin + (road_h + road_gap) * 2, road_w, road_h
road_index = 0
all_image = {}

for i in range(5):
    photo = pygame.image.load("move" + str(i) + ".png")
    fight = pygame.image.load("fight" + str(i) + ".png")
    move_wh = Image.open("move" + str(i) + ".png").size
    fight_wh = Image.open("fight" + str(i) + ".png").size
    all_image[i] = [photo, fight, move_wh, fight_wh]


class map:
    def __init__(self, model):
        self.category = category
        self.road_index = road_index
        self.model = model
        self.over = 0

    def displaySoldiers(self, army, base_hp):

        for i in army:
            photo = all_image[i.ID][0]
            fight = all_image[i.ID][1]
            move_wh = all_image[i.ID][2]
            fight_wh = all_image[i.ID][3]
            move_wh1 = move_wh[1]
            fight_wh1 = fight_wh[1]
            now_status = i.status
            if (i.flag == "right"):
                move_wh1 = move_wh1 / 2
                fight_wh1 = fight_wh1 / 2
            if i.status < 4:
                screen.blit(photo, i.pos,
                            pygame.Rect((move_wh[0] / 4) * now_status, move_wh1 / 2, move_wh[0] / 4, move_wh[1] / 4))

                # i.status = (i.status + 1) % 4
            else:
                screen.blit(fight, i.pos,
                            pygame.Rect((fight_wh[0] / 4) * (now_status - 4), fight_wh1 / 2, fight_wh[0] / 4,
                                        fight_wh[1] / 4))
                # i.status = 4 + (i.status + 1) % 4
            pygame.draw.rect(screen, (255, 0, 0), (i.pos[0], i.pos[1], 50, 4), 0)
            pygame.draw.rect(screen, (0, 255, 0), (i.pos[0], i.pos[1], 50 * (i.HP / UNIT_MAX_HP[i.ID]), 4), 0)

        pygame.draw.rect(screen, (255, 0, 0), (40, 200, 100, 6), 0)
        pygame.draw.rect(screen, (0, 255, 0), (41, 201, 98 * (base_hp[0] / BASE_MAX_HP[0]), 4), 0)
        pygame.draw.rect(screen, (255, 0, 0), (1060, 200, 100, 6), 0)
        pygame.draw.rect(screen, (0, 255, 0), (1061, 201, 98 * (base_hp[1] / BASE_MAX_HP[1]), 4), 0)

    def addSoldier(self, road_index, category):
        self.category = category
        self.road_index = road_index

    def getAttribute(self):
        return self.road_index, self.category

    def mouse_move(self, mouse_image_filename):
        mouse_cursor = pygame.image.load(mouse_image_filename)
        mouse_cursor = pygame.transform.scale(mouse_cursor, (50, 50))
        x, y = pygame.mouse.get_pos()
        # 计算光标左上角位置
        x -= mouse_cursor.get_width() / 2
        y -= mouse_cursor.get_height() / 2
        # 将光标画上去
        screen.blit(mouse_cursor, (x, y))

    def isOnclick(self):
        global category
        point_x, point_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                in_y0 = road_margin < point_y < road_margin + road_h
                in_y1 = road_margin + road_h + road_gap < point_y < road_margin + road_h + road_gap + road_h
                in_y2 = road_margin + (road_h + road_gap) * 2 < point_y < road_margin + (road_h + road_gap) * 2 + road_h

                if in_y0:
                    # 加一个兵
                    self.addSoldier(0, category)
                    self.model.add_unit(category, 0, 'left')
                    category = -1
                elif in_y1:
                    # 加一个兵
                    self.addSoldier(1, category)
                    self.model.add_unit(category, 1, 'left')
                    category = -1
                elif in_y2:
                    # 加一个兵
                    self.addSoldier(2, category)
                    self.model.add_unit(category, 2, 'left')
                    category = -1
                # row, id = game.getAttribute()
                # self.model.add_unit(id, row, 'left')

    def load_background(self, current_status):
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
        if (current_status == "left_win"):
            screen.blit(left_win_img, (350, 150))
            self.over = 1
        elif (current_status == "right_win"):
            screen.blit(right_win_img, (350, 150))
            self.over = 1

    def load_menu(self, now_cd, max_cd):
        global category
        for i in range(5):
            upImageFilename = "head" + str(i) + "0.jpg"
            downImageFilename = "head" + str(i) + "1.jpg"
            button = Button(upImageFilename, downImageFilename, (60 * (i + 1), 50), screen, category)
            cd1 = pygame.draw.rect(screen, (0, 255, 0), (60 * (i + 1) + 25, 25, 6, 50), 0)
            if (max_cd[i] - now_cd[i]):
                cd2 = pygame.draw.rect(screen, (255, 0, 0),
                                       (60 * (i + 1) + 25, 25, 6, 50 * ((max_cd[i] - now_cd[i]) / max_cd[i])), 0)
            category = button.render()
        if (category >= 0):
            mouse_image_filename = "head" + str(category) + "0.jpg"
            if(now_cd[category]==max_cd[category]):
                self.mouse_move(mouse_image_filename)
            game.isOnclick()


if __name__ == "__main__":
    model = battle_filed()
    current_status = "running"
    # unit_lists, now_cd, max_cd = model.action()
    game = map(model)
    while True:
        unit_lists, now_cd, max_cd, base_hp, current_status = model.action()

        game.load_background(current_status)
        if game.over:
            break
        game.displaySoldiers(unit_lists, base_hp)
        game.load_menu(now_cd, max_cd)
        pygame.display.update()
    while True:
        map(model).load_background(current_status)
        pygame.display.update()

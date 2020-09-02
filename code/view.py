# 游戏地图
import pygame
import sys

from button import Button
from pygame.locals import *
from PIL import Image, ImageGrab
import warnings

from battle_filed import battle_filed

ROW_Y = [310, 410, 510]


class view:
    def __init__(self):
        self.to_show_dict = {}
        self.units = []
        self.model = battle_filed()
        self.default_gui()
        self.run()

    def default_gui(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 600))

        pygame.display.set_caption("Tower game")

        map_w = 1200
        map_h = 600

        base_w = 100
        base_h = 300

        background = pygame.image.load("map.jpg")
        background = pygame.transform.scale(background, (1200, 600))

        road = pygame.image.load("road.jpg")
        r2 = road.copy()
        r3 = road.copy()

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

        self.to_show_dict[background] = (0, 0)

        self.to_show_dict[road] = pos_road1
        self.to_show_dict[r2] = pos_road2
        self.to_show_dict[r3] = pos_road3

        self.to_show_dict[base_left] = pos_base1
        self.to_show_dict[base_right] = pos_base2

    @staticmethod
    def get_unit_image(id, status):
        photo = pygame.image.load("move" + str(status) + ".png")
        fight = pygame.image.load("fight" + str(status) + ".png")

        move_wh = Image.open("move" + str(status) + ".png").size
        fight_wh = Image.open("fight" + str(status) + ".png").size

        if status < 4:
            return photo, pygame.Rect((move_wh[0] / 4) * status, move_wh[1] / 2, move_wh[0] / 4, move_wh[1] / 4)
        else:
            return fight, pygame.Rect((fight_wh[0] / 4) * (status - 4), fight_wh[1] / 2, fight_wh[0] / 4,
                                      fight_wh[1] / 4)

    def run(self):
        self.model.add_unit(0,0,'left')
        while True:
            self.units = self.model.action()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            for i, j in self.to_show_dict.items():
                self.screen.blit(i, j)

            for unit in self.units:
                pic, rec = view.get_unit_image(unit.ID, unit.status)
                self.screen.blit(pic, unit.pos, rec)

            pygame.display.update()


if __name__ == '__main__':
    v = view()

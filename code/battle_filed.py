from unit import unit
from unit_menu import unit_menu
from enemy_menu import enemy_menu
from default_data import *

DEFAULT_DISTANCE = 50
DEFAULT_ROW = [310, 410, 510]
DEFAULT_X = [100, 1100]
from base import base

POS_LEFT = 50
POS_RIGHT = 1100


class battle_filed:
    def __init__(self):
        self.unit_list = []
        self.unit_menu = unit_menu()
        self.base = {'left': base(BASE_MAX_HP[0], POS_LEFT, 'left'),
                     'right': base(BASE_MAX_HP[0], POS_RIGHT, 'right')}
        self.enemy_menu = enemy_menu()

    def action(self):
        game_statue = 'running'
        for i in self.unit_list:
            enemy, game_statue = self.check_collision(i)
            if game_statue is not 'running':
                break
            i.action(enemy)

        now_cd, max_cd = self.unit_menu.action()
        enemy_list = self.enemy_menu.action()

        for i in enemy_list:
            self.unit_list.append(i)

        dead_list = []
        for i in self.unit_list:
            if i.HP <= 0:
                dead_list.append(i)
        for i in dead_list:
            self.unit_list.remove(i)

        return self.unit_list, now_cd, max_cd, [self.base['left'].HP, self.base['right'].HP], game_statue

    def add_unit(self, no, row, flag):
        # row: 0 1 2 标记是哪三条路
        # no : 表示第几个单位
        x = DEFAULT_X[0] if flag == 'left' else DEFAULT_X[1]
        y = DEFAULT_ROW[row]

        unit = self.unit_menu.creat_unit(no, (x, y), flag)
        if unit is not None:
            self.unit_list.append(unit)

    def check_collision(self, target_unit):
        # 返回相遇对象，否则返回None
        # 注：这里最好只检查面前，以减少计算量并且避免BUG
        # 方向可以通过 unit.flag 判断
        pos = target_unit.pos
        game_statue = 'running'
        rag = DEFAULT_DISTANCE if target_unit.flag == 'left' else -DEFAULT_DISTANCE

        def is_in_range(a, b, c):
            if a < b:
                return a < c < b
            else:
                return b < c < a

        for i in self.unit_list:
            # 判定碰撞
            if i.flag != target_unit.flag and i.pos[1] == pos[1] \
                    and is_in_range(pos[0], pos[0] + rag, i.pos[0]):
                return i, game_statue

        base_flag = 'left' if 'right' == target_unit.flag else 'right'
        # 与基地发生碰撞
        if is_in_range(pos[0], pos[0] + rag, self.base[base_flag].pos):
            # 游戏状态 right_win, left_win
            self.unit_list.remove(target_unit)
            game_statue = self.base[base_flag].loss_HP(target_unit)

        return unit(100, 10, (0, 0), -1, 10, base_flag, 0, 0), game_statue

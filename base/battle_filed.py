from base.base import base

DEFAULT_DISTANCE = 50
BASE_HP = 500
POS_LEFT = 0
POS_RIGHT = 1200


class battle_filed:
    def __init__(self):
        self.unit_list = []
        self.base = {'left': base(BASE_HP, POS_LEFT, 'left'),
                     'right': base(BASE_HP, POS_RIGHT, 'right')}

    def action(self):
        for i in self.unit_list:
            enemy, game_statue = self.check_collision(i)
            i.action(enemy)

        dead_list = []
        for i in self.unit_list:
            if i.HP <= 0:
                dead_list.append(i)

        #删除del

    def check_collision(self, unit):
        # 返回相遇对象，否则返回None
        # 注：这里最好只检查面前，以减少计算量并且避免BUG
        # 方向可以通过 unit.flag 判断
        pos = unit.pos

        rag = DEFAULT_DISTANCE if unit.flag == 'left' else -DEFAULT_DISTANCE

        def is_in_range(a, b, c):
            if a < b:
                return a < c < b
            else:
                return b < c < a

        for i in self.unit_list:
            # 判定碰撞
            if i is not unit and i.pos[1] == pos[1] \
                    and is_in_range(pos[0], pos[0] + rag, i.pos[0]):
                return i

                base_flag = 'left' if 'right' == unit.flag else 'right'
                # 与基地发生碰撞
                if self.base[base_flag].pos[1] == pos[1] \
                        and is_in_range(pos[0], pos[0] + rag, self.base[base_flag].pos[0]):
                #游戏状态 right_win, left_win
                    game_statue = self.base[base_flag].loss_HP(i)

        return None, game_statue

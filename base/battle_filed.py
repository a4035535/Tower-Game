from base.unit_menu import unit_menu

DEFAULT_DISTANCE = 50
DEFAULT_ROW = [100, 200, 300]
DEFAULT_X = [100, 1100]


class battle_filed:
    def __init__(self):
        self.unit_list = []
        self.unit_menu = unit_menu()

    def action(self):
        for i in self.unit_list:
            enemy = self.check_collision(i)
            i.action(enemy)

        dead_list = []
        for i in self.unit_list:
            if i.HP <= 0:
                dead_list.append(i)
        for i in dead_list:
            self.unit_list.remove(i)
        return self.unit_list

    def add_unit(self, no, row, flag):
        # row: 0 1 2 标记是哪三条路
        # no : 表示第几个单位
        x = DEFAULT_X[0] if flag == 'left' else DEFAULT_X[1]
        y = DEFAULT_ROW[row]

        unit = self.unit_menu.creat_unit(no, (x, y), flag)

        self.unit_list.append(unit)

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
            if i is not unit and i.pos[1] == pos[1] \
                    and is_in_range(pos[0], pos[0] + rag, i.pos[0]):
                return i

        return None

DEFAULT_DISTANCE = 50


class battle_filed:
    def __init__(self):
        self.unit_list = []

    def action(self):
        for i in self.unit_list:
            enemy = self.check_collision(i)
            i.action(enemy)

        dead_list = []
        for i in self.unit_list:
            if i.HP <= 0:
                dead_list.append(i)
        while len(dead_list) != 0:
            del dead_list[0]

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
            if i is not unit and i.pos[0] == pos[0] \
                    and is_in_range(pos[1], pos[1] + rag, i.pos[1]):
                return i

        return None

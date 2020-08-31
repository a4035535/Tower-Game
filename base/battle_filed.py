class battle_filed:
    def __init__(self):
        self.unit_list = []

    def action(self):
        for i in self.unit_list:
            enemy = self.check_collision(i)
            i.action(enemy)

    def check_collision(self, unit):
        # 返回相遇对象，否则返回None
        # 注：这里最好只检查面前，以减少计算量并且避免BUG
        # 方向可以通过 unit.flag 判断
        pass
        return None

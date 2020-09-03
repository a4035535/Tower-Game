from unit import unit
from default_data import UNIT_MAX_HP


class unit_menu:
    def __init__(self):
        self.units = []
        self.cool_down = [40, 80, 80, 240, 120]
        self.now_cool_down = self.cool_down.copy()
        self.n_units = len(self.cool_down)

    def creat_unit(self, no, pos, flag):
        if self.now_cool_down[no] != self.cool_down[no]:
            return None
        else:
            self.now_cool_down[no] = 0
        hp_list = [i for i in UNIT_MAX_HP]
        if no == 0:
            return unit(hp_list[0], 10, pos, no, 10, flag, 7, 50)
        elif no == 1:
            return unit(hp_list[1], 12, pos, no, 12, flag, 5, 100)
        elif no == 2:
            return unit(hp_list[2], 20, pos, no, 15, flag, 4, 60)
        elif no == 3:
            return unit(hp_list[3], 20, pos, no, 10, flag, 4, 60)
        elif no == 4:
            return unit(hp_list[4], 15, pos, no, 10, flag, 5, 130)

        return None

    def action(self):
        for i in range(self.n_units):
            if self.now_cool_down[i] < self.cool_down[i]:
                self.now_cool_down[i] += 1

        return self.now_cool_down, self.cool_down

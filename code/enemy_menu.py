from unit_menu import unit_menu
import random

ROW_Y = [310, 410, 510]
LEVEL = 10


class enemy_menu(unit_menu):
    def __init__(self):
        super().__init__()
        self.base_cool_down = self.cool_down.copy()
        for i in range(self.n_units):
            self.base_cool_down[i] += random.randint(0, self.base_cool_down[i] * LEVEL)

    def action(self):
        enemy_list = []
        for i in range(self.n_units):
            if self.now_cool_down[i] < self.base_cool_down[i]:
                self.now_cool_down[i] += 1
            elif self.now_cool_down[i] == self.base_cool_down[i]:
                row = random.randint(0, 2)
                self.now_cool_down[i] = self.cool_down[i]
                unit = self.creat_unit(i, (1100, ROW_Y[row]), 'right')
                if unit is not None:
                    enemy_list.append(unit)

                    cool_down = self.cool_down[i]
                    self.base_cool_down[i] = cool_down + random.randint(0, cool_down * LEVEL)
        return enemy_list

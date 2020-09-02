from unit import unit


class unit_menu:
    def __init__(self):
        self.units = []
        self.cool_down = [10, 20, 30, 40, 50]
        self.now_cool_down = self.cool_down.copy()
        self.n_units = len(self.cool_down)

    def creat_unit(self, no, pos, flag):
        if self.now_cool_down[no] != self.cool_down[no]:
            return None
        else:
            self.now_cool_down[no] = 0

        if no == 1:
            return unit(100, 10, pos, 10, flag)

        return None

    def action(self):
        for i in range(self.n_units):
            if self.now_cool_down[i] < self.cool_down[i]:
                self.now_cool_down[i] += 1

        return self.now_cool_down, self.cool_down

from base.unit import unit


class unit_menu:
    def __init__(self):
        self.units = []

    def creat_unit(self, no, pos, flag):
        if no == 1:
            return unit(100, 10, pos, 10, flag)
        return None

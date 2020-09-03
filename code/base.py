class base:
    def __init__(self, HP, pos, flag):
        self.HP = HP
        self.pos = pos
        self.flag = flag

    def loss_HP(self, enemy):
        self.HP -= 100
        if self.HP <= 0:
            if self.flag == 'right':
                return 'left_win'
            else:
                return 'right_win'
        else:
            return 'running'

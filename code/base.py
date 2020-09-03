class base:
    def __init__(self, HP, pos, flag):
        self.HP = HP
        self.pos = pos
        self.flag = flag

    def loss_HP(self, enemy):
        self.HP -= enemy.ATK
        if self.HP <= 0:
            return 'left_win' if self.flag == 'right' else 'right_win'
        else:
            return 'running'

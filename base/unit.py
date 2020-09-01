

class unit:
    def __init__(self, HP, ATK, pos, attack_interval=10, flag='left'):
        self.HP = HP
        self.ATK = ATK
        # pos: (x,y) 如果不使用网格模式，直接使用图片坐标(pygame中精灵位置)
        # 否则使用 (n,m) n：第几条路  m:第几个格子
        self.pos = pos
        self.attack_interval = attack_interval
        self.now_interval = 0
        # 单位阵营
        self.flag = flag
        # status: move_1 move_2 att_1 att2
        self.status = 'move_1'



    def action(self, collision_statue):
        # 调整状态 -> 执行动作
        if collision_statue is None:
            self.move()
        elif collision_statue.flag == self.flag:
            pass
        else:
            self.attack(collision_statue)

    def move(self):
        pass

    def attack(self, enemy):
        if self.now_interval == self.attack_interval:
            enemy.HP -= self.ATK
            self.now_interval = 0
        else:
            self.now_interval += 1

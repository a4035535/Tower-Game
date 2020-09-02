class unit:
    def __init__(self, HP, ATK, pos, ID=0, attack_interval=10, flag='left'):
        self.HP = HP
        self.ATK = ATK
        # pos: (x,y) 如果不使用网格模式，直接使用图片坐标(pygame中精灵位置)
        # 否则使用 (n,m) n：第几条路  m:第几个格子
        self.pos = pos
        self.attack_interval = attack_interval
        self.now_interval = 0
        # 单位阵营
        self.flag = flag
        # status: 0~3为move_1~move_4, 4~7为att_1~att_4
        self.status = 0
        self.ID = ID

    def action(self, collision_statue):
        # 调整状态 -> 执行动作
        if collision_statue is None:
            self.move()
            if self.status <= 3:
                self.status += 1
            else:
                self.status = 0
        elif collision_statue.flag == self.flag:
            pass
        else:
            self.attack(collision_statue)
            if self.status <= 7:
                self.status += 1
            else:
                self.status = 4

    def move(self):
        self.pos = (self.pos[0]+5, self.pos[1])

    def attack(self, enemy):
        # 每10帧进行一次攻击
        if self.now_interval == self.attack_interval:
            enemy.HP -= self.ATK
            self.now_interval = 0
        else:
            self.now_interval += 1

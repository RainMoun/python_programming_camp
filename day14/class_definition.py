class Hero:
    def __init__(self, name, level, hp, q_hurt, w_hurt, e_hurt):
        self.name = name
        self.level = level
        self.hp = hp
        self.Q_hurt = q_hurt
        self.W_hurt = w_hurt
        self.E_hurt = e_hurt

    def attack(self, skill, enemy_hero):
        if skill == 'Q':
            if enemy_hero.hp > self.Q_hurt:
                enemy_hero.hp -= self.Q_hurt
                print("{} is attacked by {}, deals {} hp, his remaining hp is {}".format(enemy_hero.name, self.name,
                                                                                         self.Q_hurt, enemy_hero.hp))
            else:
                enemy_hero.hp = 0
                print("{} is skilled by {}".format(enemy_hero.name, self.name))
        elif skill == 'W':
            if enemy_hero.hp > self.W_hurt:
                enemy_hero.hp -= self.W_hurt
                print("{} is attacked by {}, deals {} hp, his remaining hp is {}".format(enemy_hero.name, self.name,
                                                                                         self.W_hurt, enemy_hero.hp))
            else:
                enemy_hero.hp = 0
                print("{} is skilled by {}".format(enemy_hero.name, self.name))
        else:
            if enemy_hero.hp > self.E_hurt:
                enemy_hero.hp -= self.E_hurt
                print("{} is attacked by {}, deals {} hp, his remaining hp is {}".format(enemy_hero.name, self.name,
                                                                                         self.E_hurt, enemy_hero.hp))
            else:
                enemy_hero.hp = 0
                print("{} is skilled by {}".format(enemy_hero.name, self.name))
import json

from class_definition import Hero

with open('hero_message.json') as f:
    hero_lst = json.load(f)
now_hero = []
for i in hero_lst:
    std_obj = Hero(i, hero_lst[i]["level"], hero_lst[i]["hp"], hero_lst[i]["Q_hurt"], hero_lst[i]["W_hurt"],
                   hero_lst[i]["E_hurt"])
    now_hero.append(std_obj)
red_camp = now_hero[0::2]
blue_camp = now_hero[1::2]
print(red_camp)
print(blue_camp)
# 对战开始
red_camp[0].attack('Q', blue_camp[1])
red_camp[1].attack('W', blue_camp[1])
blue_camp[1].attack('E', red_camp[0])
blue_camp[0].attack('W', red_camp[1])
red_camp[0].attack('Q', blue_camp[1])
red_camp[1].attack('E', blue_camp[1])
blue_camp[1].attack('E', red_camp[0])
blue_camp[0].attack('W', red_camp[1])
red_camp[0].attack('Q', blue_camp[1])
red_camp[1].attack('E', blue_camp[0])
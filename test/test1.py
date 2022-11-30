# -*- coding: UTF-8 -*-
Muk_skill=["poison jab","infestation","dark pulse","acid spray"]
Pikachu_skill=['thunder','thunderbolt','quick attatch','wild charge']
#a=input('請輸入你的名字:')
print('Muk hp:20')
print(Muk_skill)
print('pikachu hp:15')
print(Pikachu_skill)
#b=input('請選擇你要的角色:')

import random as r
class pokemon():
    def __init__(self,name):
        self.name=name
    def skill():
        pass
class Muk(pokemon):
    hp=20
    def __init__(self,name):
        super().__init__(name)
    def skill():
        i=r.randint(1,4)
        if i==1:
            Pikachu.hp=Pikachu.hp-2
        elif i==2:
            Pikachu.hp=Pikachu.hp-3
        elif i==3:
            Pikachu.hp=Pikachu.hp-4
        else:
            Pikachu.hp=Pikachu.hp-10
        print('Muk','use',Muk_skill[i-1])
class Pikachu(pokemon):
    hp=20
    def __init__(self,name):
        super().__init__(name)
    def skill():
        j=r.randint(1,4)
        if j==1:
            Muk.hp=Muk.hp-3
        elif j==2:
            Muk.hp=Muk.hp-4
        elif j==3:
            Muk.hp=Muk.hp-5
        else:
            Muk.hp=Muk.hp-10
        print('Pikachu','use',Pikachu_skill[j-1])
def pk():
    while Pikachu.hp and  Muk.hp >0:
        print("Pikachu hp:"+str(Pikachu.hp))
        Pikachu.skill()
        print('Muk.hp:'+str(Muk.hp))
        Muk.skill()
    if Pikachu.hp or Muk.hp <=0:
        if Pikachu.hp>Muk.hp:
            print('Pikachu win')
        else:
            print('Muk win')
    else:
        pass  
output=pk()

# -*- coding: UTF-8 -*-
import json
path = 'wardrobe.txt'
f = open(path, 'r')
first=input('是否要更新衣櫥:')
wardrobe=f.read()
if first=='是':
    a=input('有幾件外套:')
    b=input('有幾件短袖:')
    c=input('有幾件短褲:')
    d=input('有幾件內褲:')
    e=input('有幾雙襪子:')
    wardrobe['外套']=a
    wardrobe['短袖']=b
    wardrobe['短褲']=c
    wardrobe['內褲']=d
    wardrobe['襪子']=e
print(wardrobe)
f=int(input('今天用了幾件外套:'))
if f>0:
    k=input('是否要洗:')
    if k=='是':
       wardrobe['外套']=int(wardrobe['外套'])-f
g=int(input('今天用了幾件短袖:'))
if g>0:
    wardrobe['短袖']=int(wardrobe['短袖'])-g
h=int(input('今天用了幾件短褲:'))
if h>0:
    wardrobe['短褲']=int(wardrobe['短褲'])-h
i=int(input('今天用了幾件內褲:'))
if i>0:
    wardrobe['內褲']=int(wardrobe['內褲'])-i
j=int(input('今天用了幾雙襪子:'))
if j>0:
    wardrobe['襪子']=int(wardrobe['襪子'])-j
print('現在的庫存量',wardrobe)
path = 'wardrobe.txt'
f = open(path, 'w')
f.write(wardrobe)
f.close()



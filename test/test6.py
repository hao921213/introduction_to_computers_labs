# -*- coding: UTF-8 -*-
import json
path = 'wardrobe.txt'
f = open(path, 'r')
first=input('�O�_�n��s���o:')
wardrobe=f.read()
if first=='�O':
    a=input('���X��~�M:')
    b=input('���X��u�S:')
    c=input('���X��u��:')
    d=input('���X�󤺿�:')
    e=input('���X�����l:')
    wardrobe['�~�M']=a
    wardrobe['�u�S']=b
    wardrobe['�u��']=c
    wardrobe['����']=d
    wardrobe['���l']=e
print(wardrobe)
f=int(input('���ѥΤF�X��~�M:'))
if f>0:
    k=input('�O�_�n�~:')
    if k=='�O':
       wardrobe['�~�M']=int(wardrobe['�~�M'])-f
g=int(input('���ѥΤF�X��u�S:'))
if g>0:
    wardrobe['�u�S']=int(wardrobe['�u�S'])-g
h=int(input('���ѥΤF�X��u��:'))
if h>0:
    wardrobe['�u��']=int(wardrobe['�u��'])-h
i=int(input('���ѥΤF�X�󤺿�:'))
if i>0:
    wardrobe['����']=int(wardrobe['����'])-i
j=int(input('���ѥΤF�X�����l:'))
if j>0:
    wardrobe['���l']=int(wardrobe['���l'])-j
print('�{�b���w�s�q',wardrobe)
path = 'wardrobe.txt'
f = open(path, 'w')
f.write(wardrobe)
f.close()



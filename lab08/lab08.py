#-*- coding: UTF-8 -*-
import os#�I�sos���O
a=os.getcwd()#a����e�u�@�ؿ�
b=a.split('/')#��/���}a���F��
b.remove(b[0])#�����Ĥ@�Ӥ���
print(b)
c='/home/E94111091'#�Nc�]��path
d=os.listdir(c)#��^path�ؿ��U�Ҧ��ɮשM��Ƨ�
print(d)

path='E94111091.text'#�إߤ@�Ӥ�r�ɦW
f=open(path,'w')#�g��
for i in range(len(b)):
    f.write(b[i])
    f.write(os.linesep)#�Nb���������@�Ӭ��@��g�J��r��
f.write(os.linesep)
for j in range(len(d)):
    f.write(d[j])
    f.write(os.linesep)#�Nd���������@�Ӭ��@��g�J��r��
f.close()#����

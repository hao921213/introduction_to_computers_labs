# -*- coding: UTF-8 -*-
import json
def eee(input):#�إߤ@�Ө��
    f=list(input[0])#f���U�D���魫 
    limit=input[1]#limit���U�D������
    c=f#��������f�A�����ٻݭn��
    b=max(f)#����Xf���̤j���Ʀr
    while True:#�P�_���G�O�_�blimit�̭�
        c=[]#�إߤ@��list
        a=0#�]�@���ܼ�a��0�Aa�@���ۥ[���e��
        d=0#�]�@���ܼ�d��0,d�D�n�O�n�Ψӧ@��index�ޥX�n���Ʀr
        while d<len(f):#��d�b�p���魫�`�ƪ����p�U����A���I����for��for�S��k���ư���j��
           a+=f[d]
           if a>b:#�p�Ga�j��̤j�魫
               a-=f[d]#����@�}�l�[��
               if d==len(f)-1:#�p�G��n�[��̫�@�ӼơA�h��Ӥ��}�A�A�[�Jlist��
                   c.append(f[d])
                   c.append(a)
                   break#���槹�N�����j��
               c.append(a)#�A�[�ilist�̭��x�s
               a=0#�[���᭫�sa
           elif a==b:#�p�Ga==b
               if d==len(f)-1:#�p�G��n�[��̫�@�ӼơA�h�����[�Jlist��
                   c.append(a)
                   break
               c.append(a)#�����[�i�hlist���δ�h�[�J���Ʀr
               a=0
               d+=1#�Od�[�@�A����U�@��
           else:#�p�󪺸ܡA�h��������U�@���A���D�O�̫�@�Ӽ�
               if d==len(f)-1:#�p�G��n�[��̫�@�ӼơA�h�����[�Jlist��
                   c.append(a)
                   break
               d+=1
        b+=1#�O�̤j�ӭ��[1�C�C��X�̤p�ӭ�
        if len(c)<=limit:#�p�Gc�����פj��limit�h���s�^��
            break
    global e
    e=max(c)
    return e            
with open('input_plus.json', 'r') as inputFile:
    data = json.load(inputFile)
    for key in data:
        input = data[key]
        c=eee(input)
        print('Question: ' + str(key))
        print('Answer:', e)
        print()
        

# -*- coding: UTF-8 -*-
import json
def BF(input):
    N=len(input)
    d=list(input)
    c=[]
    Sum1=[]
    Sum2=[]
    list1=[]
    assignment_all=[]
    cost_all=[]
    dict1={}
    for l in range(0,N):
        c.append(l)
    def perm(n,a,b):#���ƦC���        
        if a>=b:
            global z
            z=list(n)
            assignment_all.append(z)#�N���ƦC�s�Jassignment_all
            for m in range(0,N):         
              Sum1.append(d[c[m]][n[m]]) #�N�ƦC��L�쪺�u�@�Ӯ��x�s�bSum1                                              
        else:
            i=a
            for num in range(a,b):
                n[num],n[i]=n[i],n[num]
                perm(n,a+1,b)
                n[num],n[i]=n[i],n[num]                   
    n=[]#�w���D�ػݨD�i��X�����ƶq�����ƦC�A�Ҧp4��N�O0123
    for k in range(0,N):
        n.append(k)
    perm(n,0,len(n))#������ƦC
    for e in range(1,len(Sum1)+1):#�N�Ҧ��u�@�Ӯɦs�blist1�A�A����s�bSum2
        list1.append(Sum1[e-1])
        if len(list1)>N-1:
            Sum2.append(list1)
            list1=[]
    print(Sum1,Sum2)
    for f in range(1,len(Sum2)+1):#�O�C��ۥ[�A�æs�bcost_all
        h=0
        for g in range(N):
            h+=Sum2[f-1][g]
        cost_all.append(h)
    cost=min(cost_all)#���̤p��
    for f in range(1,len(Sum2)+1):#�إߤ@�Ӧr��A��K��X
        dict1[cost_all[f-1]]=assignment_all[f-1]
    assignment=dict1[cost]#��̤pcost�ɪ�assignment
    return assignment, cost                   
with open('input.json', 'r') as inputFile:
    data = json.load(inputFile)
    for key in data:
        input = data[key] 
        assignment, cost = BF(input)
        print('Question: ' + str(key))
        print('Assignment:', assignment)
        print('Cost:', cost)
        print()
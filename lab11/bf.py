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
    def perm(n,a,b):#全排列函數        
        if a>=b:
            global z
            z=list(n)
            assignment_all.append(z)#將全排列存入assignment_all
            for m in range(0,N):         
              Sum1.append(d[c[m]][n[m]]) #將排列對印到的工作耗時儲存在Sum1                                              
        else:
            i=a
            for num in range(a,b):
                n[num],n[i]=n[i],n[num]
                perm(n,a+1,b)
                n[num],n[i]=n[i],n[num]                   
    n=[]#針對題目需求可找出足夠數量的全排列，例如4格就是0123
    for k in range(0,N):
        n.append(k)
    perm(n,0,len(n))#執行全排列
    for e in range(1,len(Sum1)+1):#將所有工作耗時存在list1，再分堆存在Sum2
        list1.append(Sum1[e-1])
        if len(list1)>N-1:
            Sum2.append(list1)
            list1=[]
    print(Sum1,Sum2)
    for f in range(1,len(Sum2)+1):#令每堆相加，並存在cost_all
        h=0
        for g in range(N):
            h+=Sum2[f-1][g]
        cost_all.append(h)
    cost=min(cost_all)#找到最小值
    for f in range(1,len(Sum2)+1):#建立一個字典，方便輸出
        dict1[cost_all[f-1]]=assignment_all[f-1]
    assignment=dict1[cost]#找最小cost時的assignment
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
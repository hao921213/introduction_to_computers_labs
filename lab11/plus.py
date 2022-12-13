# -*- coding: UTF-8 -*-
import json
def eee(input):#建立一個函數
    f=list(input[0])#f為各題的體重 
    limit=input[1]#limit為各題的限制
    c=f#先讓等於f，後續還需要用
    b=max(f)#先找出f中最大的數字
    while True:#判斷結果是否在limit裡面
        c=[]#建立一個list
        a=0#設一個變數a為0，a作為相加的容器
        d=0#設一個變數d為0,d主要是要用來作為index引出要的數字
        while d<len(f):#讓d在小於體重總數的情況下執行，有點類似for但for沒辦法重複執行迴圈
           a+=f[d]
           if a>b:#如果a大於最大體重
               a-=f[d]#先減掉一開始加的
               if d==len(f)-1:#如果剛好加到最後一個數，則兩個分開，再加入list裡
                   c.append(f[d])
                   c.append(a)
                   break#執行完就結束迴圈
               c.append(a)#再加進list裡面儲存
               a=0#加完後重製a
           elif a==b:#如果a==b
               if d==len(f)-1:#如果剛好加到最後一個數，則直接加入list裡
                   c.append(a)
                   break
               c.append(a)#直接加進去list不用減去加入的數字
               a=0
               d+=1#令d加一，執行下一輪
           else:#小於的話，則直接執行下一輪，除非是最後一個數
               if d==len(f)-1:#如果剛好加到最後一個數，則直接加入list裡
                   c.append(a)
                   break
               d+=1
        b+=1#令最大承重加1慢慢找出最小承重
        if len(c)<=limit:#如果c的長度大於limit則重新回圈
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
        

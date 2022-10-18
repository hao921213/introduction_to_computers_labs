import random as r#命令指令
Times={'one':0,'two':0,'three':0,'four':0,'five':0,'six':0}#建立一個字典和list,等等輸出比較方便
list1=list(Times.keys())
for i in range(1000000):#重複1000000次
    i=r.randint(1,6)#隨機從1到6取一個數
    m=i-1
    Times[list1[m]]=Times[list1[m]]+1#令抽到的那個數加一
for j in range(0,6):#重複6次
    k=Times[list1[j]]
    n=(int(k)/1000000*100)#算機率
    l=round(n,2)#取到小數點後第二位
    print('The probability of'+' '+list1[j]+' '+'is'+' '+str(l)+'%')#輸出結果
    
    
    

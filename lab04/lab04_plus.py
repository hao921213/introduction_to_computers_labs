A=[]
B=[]
C=[]
score=[A,B,C]
subject=['國文','英文','數學','自然','社會']
name=['A','B','C']
for i in range(0,3):
    print('請輸入'+name[i]+'學生的成績請依照國文,英文,數學,自然,社會:')
    for j in range(0,5):
        num=input()
        num=int(num)
        score[i].append(num)
        while num>100 or num<=0:#當在範圍外時
            print('請輸入1-100')#印出請輸入1-100
            score[i].pop()#減去超出範圍的值
            num=input()#重新輸入
            num=int(num)#改為整數
            score[i].append(num)
            if num<=100 and  num>0:#如果在範圍內
                score[i].append(num)#加入list
                break#結束while
    print(name[i]+'學生成績:')
    print('國文:'+str(score[i][0])+'英文:'+str(score[i][1])+'數學:'+str(score[i][2])+'自然:'+str(score[i][3])+'社會:'+str(score[i][4]))
for i in range(0,3):
    score_num=(int(x) for x in score[i])
    average=str(sum(score_num)/len(score))
    print(name[i]+'學生平均成績'+average)
for j in range(0,5):
    A_sub=[int(x) for x in A]
    B_sub=[int(x) for x in B]
    C_sub=[int(x) for x in C]
    sub_aver=(A_sub[j]+B_sub[j]+C_sub[j])/3
    print(subject[j]+'成績平均'+str(sub_aver))

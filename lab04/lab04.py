A=[]
B=[]
C=[]#定義A,B,C為list
score=[A,B,C]#定義score為裝入A,B,C的list(二維陣列)
subject=['國文','英文','數學','自然','社會']#定義subject為科目字串的list
name=['A','B','C']#定義name為A,B,C字串的list
for i in range(0,3):#建立一個重複三次的迴圈
    print('請輸入'+name[i]+'學生的成績,請依照國文,英文,數學,自然,社會:')#輸出一開始輸入的成績
    for j in range(0,5):#建立一個重複五次的迴圈
        number=input()#定義number為輸入值
        score[i].append(number)#將輸入值加入score
    print(name[i]+'學生成績:')#輸出某學生成績:
    print('國文:'+score[i][0]+'英文:'+score[i][1]+'數學:'+score[i][2]+'自然:'+score[i][3]+'社會:'+score[i][4])#輸出各科成績
for i in range(0,3):
    score_num=(int(x) for x in score[i])#定義score_num為輸入值,並轉換成整數
    average=str(sum(score_num)/len(score))#定義average為總和除個數並轉換成字串
    print(name[i]+'同學的平均成績:'+average)#輸出平均成績
for j in range(0,5):
    A_sub=[int(x) for x in A]
    B_sub=[int(x) for x in B]
    C_sub=[int(x) for x in C]
    sub_aver=(A_sub[j]+B_sub[j]+C_sub[j])/3
    print(subject[j]+'的平均成績'+str(sub_aver))#輸出各科平均成績





subject=['國文','英文','數學','自然','社會']
A=['50','60','70','80','90']
B=['57','86','73','82','43']
C=['97','96','86','97','83']#將subject A B C定義為list
dict0=dict([['index',subject],['StuA',A],['StuB',B],['StuC',C]])#dict0定義為字典
print('dict0:')#輸出'dict0':
print(dict0)#輸出dict0
name=['A','B','C']#將name定義為list裝入'A' 'B' 'C'
score=[A,B,C]#將score定義為list裝入A B C三個list
for i in range(0,3):#設立一個重複三次的迴圈
    score_num=[int(x) for x in score[i]]#將score_num定義為把A B C內的元素轉化為整數
    aver=str(sum(score_num)/len(score_num))#將aver定義為求平均並轉換成字串
    print(name[i]+'學生的平均成績:'+aver)

for j in range(0,5):
    A_num=[int(x) for x in A]
    B_num=[int(x) for x in B]
    C_num=[int(x) for x in C]
    sub_aver=(A_num[j]+B_num[j]+C_num[j])/3
    print(subject[j]+'平均成績:'+str(sub_aver))



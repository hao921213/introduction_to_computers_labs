import random as r
a=['誰?','為甚麼我要知道他','喔是喔沒興趣','又不紅']
b=['笑死','有料ㄛ','確實','哈哈哈']
c=['隨便','我還沒想到','都可以','看你阿']
print('1為網路上或新聞出現了你看都沒看過的網紅或藝人')
print('2為當有一個你連理都不想理的人一直煩你,但為了維持好形象你又必須回他')
print('3為室友問你等等要吃甚麼')
q=input('請輸入你的情況:')
s=int(q)
if s==1:
    i=r.randint(1,4)
    print(a[i-1]) 
elif s==2:
    j=r.randint(1,4)
    print(b[j-1])
elif s==3:
    k=r.randint(1,4)
    print(c[k-1])







import random as r
a=input('請輸入想吃得消夜:')
print('剪刀石頭布!')
for i in range(3):
    d=r.randint(1,3)
    e=int(input('請輸入 1=剪刀 2=拳頭 3=布:'))
    if d==e:
        print('成功')
    else:
        print('失敗')
        break


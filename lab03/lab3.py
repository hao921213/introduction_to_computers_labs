a=input("please input your student ID first character:")#將a設為please input your student ID first character:
b=input('please input your student ID last 8 number:')#將b設為please input your student ID last 8 number:
c=int(b)#把b強行轉換為整數才可以加減乘除
if c%2==1:
    print('奇數')#如果b除2餘式是1則印出'奇數'
else :
    print("偶數")#否則印出'偶數'
print("your student ID="+a+b)#印出a(學號第一個字母)跟b(學號後八碼)


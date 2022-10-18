def gcd (a,b):#建立一個函數為gcd,參數是(a,b)
    l,i=a,b#用l,i取代a,b
    if l==0 or i==0:
        print('0沒有gcd')
        return 0#如果l,i其中有一個為0,則輸出0沒有gcd,並回傳0停止指令
    if i>l:
        l,i=i,l#如果i>l的話,則將兩個對調,才能做除法
    m,n=l,i#用m,n取代l,i,如果不取代，下方運算式才不會有事
    while m%n!=0:
        r=m%n
        m=i
        n=r#如果m除n的餘數不為0,則將m換成i,n換成m除n並重新運算直到條件達成
    if n!=1:
        print(str(a)+'和'+str(b)+'的gcd='+str(n))
    else:
        print(str(a)+'和'+str(b)+'互質')#如果n不等於1則輸出a,b的最大公因數，否則輸出a,b互質
ans1=gcd(80,20)#參數
ans2=gcd(10,0)
ans3=gcd(19,20)

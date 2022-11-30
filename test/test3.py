a=input('請輸入需要的字數:')
b=input('請輸入文章或回答(標點符號後請空一格):')
e=input('是否需要顯示字數:')
c=b.split()
if int(a)>len(c):
    print('你還差'+str(int(a)-len(c)))
elif int(a)<len(c):
    print('字數已足夠')
elif int(a)==len(c):
    print('太神辣,字數人')
if e=='是':
    print('你的字數是:'+str(len(c)))
elif e=='否':
    pass

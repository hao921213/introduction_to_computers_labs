print('ax^2+bx+c')
a=int(input('請輸入a值:'))
b=int(input('請輸入b值:'))
c=int(input('請輸入c值:'))
d=b**2-4*a*c
if d<0:
    print('無實數解')
else:
    print(str((-b+d**(1/2))/2*a))
    print(str((-b-d**(1/2))/2*a))

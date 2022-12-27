import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
text=[]
a=[]
b=[]
f = open('oddExperiment.txt','r')
for line in f.readlines():
    line=line.replace('\n','')
    line=line.replace(',','')
    line=line.split(' ')
    text.append(line)
del text[0]
for i in range(21):
    a.append(float(text[i][0]))
    b.append(int(text[i][1]))
plt.scatter(b,a,label='Data')
parameter=np.polyfit(b,a,1)
p = np.poly1d(parameter)
parameter2=np.polyfit(b,a,2)
p2 = np.poly1d(parameter2)
c=round(r2_score(a,p(b)),5)
d=round(r2_score(a,p2(b)),5)
e=round(mean_squared_error(a,p(b)),5)
g=round(mean_squared_error(a,p2(b)),5)
plt.plot(0,0,label='Fit of degree 1,LSE='+str(e),color='orange')
plt.plot(0,0,label='Fit of degree 2,LSE='+str(g),color='green')
plt.plot(b,p(b),label='Fit of degree 1,R2='+str(c),color='red')
plt.plot(b,p2(b),label='Fit of degree 2,R2='+str(d),color='purple')
plt.title('oddExperiment Data')
plt.legend(loc='upper center')
plt.savefig('lab13_plus')
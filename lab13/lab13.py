import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
f = open('Temperature.txt')
text=[]
a = [1,2,3,4,5,6,7,8,9,10,11,12]
b=[]
z=[]
ave=[]
year= np.array(range(2013,2022))
next(f)
for line in f.readlines():
    line=line.replace('\n','')
    line=line.replace(',','')
    line=line.split(' ')
    text.append(line)
for i in range(9):
    del text[i][0]
for j in range(9):
    b=[]
    for k in range(12):
        b.append(float(text[j][k]))
    plt.plot(a,b,label=year[j])
plt.xticks(range(1,13))
plt.xlabel('month')
plt.ylabel('Temperature in Degree C')
plt.title('Tainan Monthly Mean Temperatur From 2013 To 2021')
plt.legend(loc='lower center')
plt.savefig('lab13_01')

fig = plt.figure()
f = open('Temperature.txt')
text=[]
a = [1,2,3,4,5,6,7,8,9,10,11,12]
b=[]
ave=[]
year= np.array(range(2013,2022))
next(f)
for line in f.readlines():
    line=line.replace('\n','')
    line=line.replace(',','')
    line=line.split(' ')
    text.append(line)
for i in range(9):
    del text[i][0]
for j in range(12):
    for k in range(9):
        b.append(float(text[k][j]))
    c=sum(b)/9
    ave.append(c)
    b=[]
plt.plot(a,ave,marker='o',markeredgecolor='r',markerfacecolor='r')
d=round(sum(ave)/12,2)
plt.text(1,d,d)
for d,e in zip(a,ave):
    plt.text(d,e,round(e,2),horizontalalignment='center')   
plt.ylim(16,32)
plt.xticks(range(1,13))
plt.axhline(y=sum(ave)/12, xmin=0, xmax=12,color='r',label='Mean of 9 years',linestyle="--")
plt.title('Tainan Monthly Mean Temperatur Of 2013 To 2021')
plt.xlabel('month')
plt.ylabel('Temperature in Degree C')
plt.legend()
plt.savefig('lab13_02')
fig = plt.figure(figsize=(15,6))
fig.add_subplot(1, 2, 1)
plt.subplot(1, 2, 1)
f = open('Temperature.txt')
text=[]
a = [1,2,3,4,5,6,7,8,9,10,11,12]
year= np.array(range(2013,2022))
next(f)
for line in f.readlines():
    line=line.replace('\n','')
    line=line.replace(',','')
    line=line.split(' ')
    text.append(line)
for i in range(9):
    del text[i][0]
for j in range(9):
    b=[]
    for k in range(12):
        b.append(float(text[j][k]))
    plt.plot(a,b,label=year[j])
plt.xticks(range(1,13))
plt.xlabel('month')
plt.ylabel('Temperature in Degree C')
plt.title('Tainan Monthly Mean Temperatur From 2013 To 2021')
plt.legend(loc='lower center')


plt.subplot(1,2,2)
f = open('Temperature.txt')
text=[]
a = [1,2,3,4,5,6,7,8,9,10,11,12]
b=[]
ave=[]
year= np.array(range(2013,2022))
next(f)
for line in f.readlines():
    line=line.replace('\n','')
    line=line.replace(',','')
    line=line.split(' ')
    text.append(line)
for i in range(9):
    del text[i][0]
for j in range(12):
    for k in range(9):
        b.append(float(text[k][j]))
    c=sum(b)/9
    ave.append(c)
    b=[]
plt.plot(a,ave,marker='o',markeredgecolor='r',markerfacecolor='r')
d=round(sum(ave)/12,2)
plt.text(1,d,d)
for d,e in zip(a,ave):
    plt.text(d,e,round(e,2),horizontalalignment='center')   
plt.ylim(16,32)
plt.xticks(range(1,13))
plt.axhline(y=sum(ave)/12, xmin=0, xmax=12,color='r',label='Mean of 9 years',linestyle="--")
plt.title('Tainan Monthly Mean Temperatur Of 2013 To 2021')
plt.xlabel('month')
plt.ylabel('Temperature in Degree C')
plt.legend()

fig.savefig('lab13_03.png')
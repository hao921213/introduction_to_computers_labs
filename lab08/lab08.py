import os
a=os.getcwd()
b=a.split('/')
b.remove(b[0])
print(b)
c='/home/E94111091'
d=os.listdir(c)
print(d)

path='E94111091.text'
f=open(path,'w')
for i in range(len(b)):
    f.write(b[i])
    f.write(os.linesep)
f.write(os.linesep)
for j in range(len(d)):
    f.write(d[j])
    f.write(os.linesep)
f.close()

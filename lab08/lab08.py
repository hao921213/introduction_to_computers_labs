#-*- coding: UTF-8 -*-
import os#呼叫os指令
a=os.getcwd()#a為當前工作目錄
b=a.split('/')#用/分開a的東西
b.remove(b[0])#移除第一個元素
print(b)
c='/home/E94111091'#將c設為path
d=os.listdir(c)#返回path目錄下所有檔案和資料夾
print(d)

path='E94111091.text'#建立一個文字檔名
f=open(path,'w')#寫檔
for i in range(len(b)):
    f.write(b[i])
    f.write(os.linesep)#將b中的元素一個為一行寫入文字檔
f.write(os.linesep)
for j in range(len(d)):
    f.write(d[j])
    f.write(os.linesep)#將d中的元素一個為一行寫入文字檔
f.close()#關閉

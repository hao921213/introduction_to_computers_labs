from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)#基本
dic1={}
list2=[]
list3=[]#建立兩個list裝key跟value一個字典裝key跟value
for i in range(len(list2)):#把變數輸入到字典裡
  dic1[list2[i]]=list3[i]
@app.route('/',methods=['GET'])#輸入這個網址，會回傳ok
def root():
    return 'ok'
@app.route('/set',methods=['POST'])#輸入這個網址，可以輸入變數，如果有重複的key會回傳key已存在
def root1():
    a = request.form.to_dict()
    list1=list(a.values())
    b=list1[0] in list2#判斷是否有重複
    if b==True:
      return 'key exist'
    else:
      list2.append(list1[0])
      list3.append(list1[1])
      for i in range(len(list2)):#刷新一下字典
        dic1[list2[i]]=list3[i]
      return 'set seccess'
@app.route('/key_list',methods=['GET'])
def root2():#輸入這個網址，可已回傳已存在的key
    list4=list(dic1.keys())
    return str(list4)
@app.route('/get_value/<key>',methods=['GET'])#輸入這個網址，可得到value
def root3(key):
    a = key
    b=a in list2#判斷有沒有這個key，
    list4=list(dic1.keys())
    if len(list4)==0:#如果根本沒有key，回傳key not found
      return 'key not found'
    if b==True:
      c=dic1.get(a)
      return c
    else:
      return 'key not found'
@app.route('/update_value',methods=['POST'])#輸入這個網址，可刷新
def root4():
    a = request.form.to_dict()
    list1=list(a.values())
    b=list1[0] in list2
    c=list1[1]
    if b==True:
      e=list2.index(list1[0])
      dic1[list1[0]]=list1[1]#刷新字典
      return 'update success'
    else:
      return 'key does not exist'
@app.route('/delete/<key>',methods=['GET'])#輸入這個網址,可以刪除key,value
def root5(key):
   a = key
   b=a in list2
   if b==True:
     del dic1[a]
     return 'delete success'
   else:
     return 'key not found'
app.run(host="0.0.0.0", port=3000, debug=True)

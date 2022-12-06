from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)#��
dic1={}
list2=[]
list3=[]#�إߨ��list��key��value�@�Ӧr���key��value
for i in range(len(list2)):#���ܼƿ�J��r���
  dic1[list2[i]]=list3[i]
@app.route('/',methods=['GET'])#��J�o�Ӻ��}�A�|�^��ok
def root():
    return 'ok'
@app.route('/set',methods=['POST'])#��J�o�Ӻ��}�A�i�H��J�ܼơA�p�G�����ƪ�key�|�^��key�w�s�b
def root1():
    a = request.form.to_dict()
    list1=list(a.values())
    b=list1[0] in list2#�P�_�O�_������
    if b==True:
      return 'key exist'
    else:
      list2.append(list1[0])
      list3.append(list1[1])
      for i in range(len(list2)):#��s�@�U�r��
        dic1[list2[i]]=list3[i]
      return 'set seccess'
@app.route('/key_list',methods=['GET'])
def root2():#��J�o�Ӻ��}�A�i�w�^�Ǥw�s�b��key
    list4=list(dic1.keys())
    return str(list4)
@app.route('/get_value/<key>',methods=['GET'])#��J�o�Ӻ��}�A�i�o��value
def root3(key):
    a = key
    b=a in list2#�P�_���S���o��key�A
    list4=list(dic1.keys())
    if len(list4)==0:#�p�G�ڥ��S��key�A�^��key not found
      return 'key not found'
    if b==True:
      c=dic1.get(a)
      return c
    else:
      return 'key not found'
@app.route('/update_value',methods=['POST'])#��J�o�Ӻ��}�A�i��s
def root4():
    a = request.form.to_dict()
    list1=list(a.values())
    b=list1[0] in list2
    c=list1[1]
    if b==True:
      e=list2.index(list1[0])
      dic1[list1[0]]=list1[1]#��s�r��
      return 'update success'
    else:
      return 'key does not exist'
@app.route('/delete/<key>',methods=['GET'])#��J�o�Ӻ��},�i�H�R��key,value
def root5(key):
   a = key
   b=a in list2
   if b==True:
     del dic1[a]
     return 'delete success'
   else:
     return 'key not found'
app.run(host="0.0.0.0", port=3000, debug=True)

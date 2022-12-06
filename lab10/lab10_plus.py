from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
path = 'output.txt'
f = open(path, 'w')
dic1={}
list2=[]
list3=[]
for i in range(len(list2)):
  dic1[list2[i]]=list3[i]
@app.route('/',methods=['GET'])
def root():
    return 'ok'
@app.route('/set',methods=['POST'])
def root1():
    a = request.form.to_dict()
    list1=list(a.values())
    b=list1[0] in list2
    if b==True:
      return 'key exist'
    else:
      list2.append(list1[0])
      list3.append(list1[1])
      for i in range(len(list2)):
        dic1[list2[i]]=list3[i]
      f.write(dic1.split)
      return 'set seccess'
@app.route('/key_list',methods=['GET'])
def root2():
    list4=list(dic1.keys())
    return str(list4)
@app.route('/get_value/<key>',methods=['GET'])
def root3(key):
    a = key
    b=a in list2
    list4=list(dic1.keys())
    if len(list4)==0:
      return 'key not found'
    if b==True:
      c=dic1.get(a)
      return c
    else:
      return 'key not found'
@app.route('/update_value',methods=['POST'])
def root4():
    a = request.form.to_dict()
    list1=list(a.values())
    b=list1[0] in list2
    c=list1[1]
    if b==True:
      e=list2.index(list1[0])
      dic1[list1[0]]=list1[1]
      return 'update success'
    else:
      return 'key does not exist'
@app.route('/delete/<key>',methods=['GET'])
def root5(key):
   a = key
   b=a in list2
   if b==True:
     e=list2.index(a)
     del dic1[a]
     return 'delete success'
   else:
     return 'key not found'
app.run(host="0.0.0.0", port=3000, debug=True)

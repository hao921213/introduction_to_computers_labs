#新竹市人口統計表
#https://data.gov.tw/dataset/67531
#第一筆資料是我在測試的時候不小心弄上去的，但我不會刪，請助教諒解
import requests
import pymysql
r = requests.get('https://odws.hccg.gov.tw/001/Upload/25/opendataback/9059/57/320c9e83-5d8b-4754-8449-e092a55e79c6.json')
a = r.json()

for j in range(15):
    connectdb=pymysql.connect(host='localhost',user='e94111091',password='1024',charset='utf8mb4',db='wordpress')
    with connectdb.cursor() as cursor:
        b=[i['人口數'] for i in a]
        c=[i['遷入人數'] for i in a]
        d=[i['出生人數'] for i in a]
        e=[i['結婚對數'] for i in a]
        cursor.execute('''INSERT INTO 新竹市人口統計表 values(%s,%s,%s,%s)''', (b[j],c[j],d[j],e[j]))
        connectdb.commit()
connectdb.close()

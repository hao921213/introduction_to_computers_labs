class Animals():#建立一個class叫Animals
    def __init__(self,weight,mood):#初始化
        self.weight=weight
        self.mood=mood#定義屬性
    def feed(self):#建立一個method
        pass#略過
    def walk(self):
        pass
    def bath(self):
        pass
class Dogs(Animals):#建立一個animals的子類別
    def __init__(self,weight,mood):
        self.weight=weight
        self.mood=mood
    def feed(self):
        self.weight+=0.2
        self.mood=self.mood+1#當用到feed這個method執行weight,height進行運算
    def walk(self):
        self.weight-=0.2
        self.mood=self.mood+2
    def bath(self):
        self.mood=self.mood-2
    def printf(self,n_feed,n_walk,n_bath):
        self.n_feed=n_feed
        self.n_walk=n_walk
        self.n_bath=n_bath
        for a in range(n_feed):
            Dogs.feed(self)
        for b in range(n_walk):
            Dogs.walk(self)
        for c in range(n_bath):
            Dogs.bath(self)#用到printf這個method時,會產生輸入參數的回圈,會重複執行上面三個method
        print('狗狗現在的體重='+str(self.weight)+','+'心情='+str(self.mood))#輸出結果
class Shiba(Dogs):#建立一個dogs的子類別
    def __init__(self,weight,mood):
        self.weight=weight
        self.mood=mood
    def feed(self):
        self.weight=self.weight+0.3
        self.mood=self.mood+5
    def printf(self,n_feed,n_walk,n_bath):
        self.n_feed=n_feed
        self.n_walk=n_walk
        self.n_bath=n_bath
        for d in range(n_feed):
            Shiba.feed(self)
        for e in range(n_walk):
            Dogs.walk(self)
        for f in range(n_bath):
            Dogs.bath(self)
        print('柴犬現在的體重='+str(self.weight)+','+'心情='+str(self.mood))
    def mood_constraint(self,constraint):#建立一個函數,用來限制心情
        self.constraint=constraint
        print('mood最高只能為'+str(self.constraint))#輸出心情最大值
        if self.mood>self.constraint:
            print('所以,現在柴犬的心情='+str(self.constraint))#如果原本的心情大於限制值,則會強制調整為最大值即限制值
shiba=Shiba(5,70)
shiba.printf(20,10,3)
shiba.mood_constraint(90)
shiba.mood_constraint(300)


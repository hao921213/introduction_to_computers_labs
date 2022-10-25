class Animals():#建立一個class叫Animals
    def __init__(self,weight,mood):#初始化數值
        self.weight=weight#定義屬性
        self.mood=mood
    def feed(self):#建立一個method
        pass
    def walk(self):
        pass
    def bath(self):
        pass
class Dogs(Animals):#建立一個animals的子類別
    def __init__(self,weight,mood):
        self.weight=weight
        self.mood=mood
    def feed(self):#執行這個函數時,對weight,height做運算
        self.weight=self.weight+0.2
        self.mood=self.mood+1
    def walk(self):
        self.weight=self.weight-0.2
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
            Dogs.bath(self)#用printf這個函數時,產生一個參數次的迴圈並執行迴圈內的函數
        print('狗狗現在的體重='+str(self.weight)+','+'心情='+str(self.mood))#輸出結果
class Cats(Animals):
    def __init__(self,weight,mood):
        self.weight=weight
        self.mood=mood
    def feed(self):
        self.weight=self.weight+0.1
        self.mood=self.mood+1
    def walk(self):
        self.weight=self.weight-0.1
        self.mood=self.mood-1
    def bath(self):
        self.mood=self.mood-2
    def printf(self,n_feed,n_walk,n_bath):
        self.n_feed=n_feed
        self.n_walk=n_walk
        self.n_bath=n_bath
        for d in range(n_feed):
            Cats.feed(self)
        for e in range(n_walk):
            Cats.walk(self)
        for f in range(n_bath):
            Cats.bath(self)
        print('貓貓現在的體重='+str(self.weight)+','+'心情='+str(self.mood))
dog=Dogs(4.8,65)
dog.printf(18,10,4)
cat=Cats(8.2,60)
cat.printf(40,7,1)



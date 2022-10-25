class Animals():
    def __init__(self,weight,mood):
        self.weight=weight
        self.mood=mood
    def feed(self):
        pass
    def walk(self):
        pass
    def bath(self):
        pass
class Dogs(Animals):
    def __init__(self,weight,mood):
        self.weight=weight
        self.mood=mood
    def feed(self):
        self.weight=weight+0.2
        self.mood=mood+1
    def walk(self):
        self.weight=weight-0.2
        self.mood=mood+2
    def bath(self):
        self.mood=mood-2
    def printf(self,n_feed,n_walk,n_bath):
        self.n_feed=n_feed
        self.n_walk=n_walk
        self.n_bath=n_bath
        print('狗狗現在的體重='+str(self.weight)+','+'心情='+str(self.mood))
class Cats(Animals):
    def __init__(self,weight,mood):
        self.weight=weight
        self.mood=mood
    def feed(self):
        self.weight=weight+0.1
        self.mood=mood+1
    def walk(self):
        self.weight=weight-0.1
        self.mood=mood-1
    def bath(self):
        self.mood=mood-2
    def printf(self,n_feed,n_walk,n_bath):
        self.n_feed=n_feed
        self.n_walk=n_walk
        self.n_bath=n_bath
        print('貓貓現在的體重='+str(self.weight)+','+'心情='+str(self.mood))
dog=Dogs(4.8,65)
dog.printf(18,10,4)
cat=Cats(8.2,60)
cat.printf(40,7,1)



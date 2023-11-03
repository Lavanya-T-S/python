class Lavu:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
    def kusu(self):
        print("my name is "+self.name+ " favourite colour is " +self.color)
chethu=Lavu("jasmine",20,"yellow")
chethu.kusu()
class Computer:
    def __init__(self):
        self.name="lavu"
        self.age=22
    def compare(self,c2):#compare connsits of two arguments compae(who is calling,whom to compare)
        if c1.age==c2.age:
            print('age is same')
        else:
            print('age is different' )


c1=Computer()
c1.name="kusu"
c2=Computer()
c1.compare(c2)
    #print('they are same')

print(c1.name)
print(c2.name)

output:
C:\Users\ADMIN\.virtualenvs\sample\Scripts\python.exe C:\Users\ADMIN\PycharmProjects\pythonProject1\sample\compare.py 
age is same
kusu
lavu
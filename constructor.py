class Robot:
    def __init__(self,n,w,c):#constructor creation
        self.name=n
        self.weight=w
        self.color=c
    def introduce_self(self):#method
        print("my name is "+ self.name)
r1=Robot("tom",30,"red")#object creation
r2=Robot("Jerry",40,"blue")#object creation
r1.introduce_self()#object.function calling --->function calling
r2.introduce_self()

class Person:#class
    def __init__(self,n,p,i):#constructor
        self.name=n
        self.personality=p
        self.is_sitting=i

    def sit_down(self):
        self.is_sitting=True

    def stand_up(self):
        self.is_sitting=False

p1=Person("Alice","aggeresive",False)#object creation
p2=Person("rocky","talkative",True)#object creation
p1.robot_owned=r2#object.class name=obejct
p2.robot_owned=r1
p1.robot_owned.introduce_self()#object.class name.method name


output:


C:\Users\ADMIN\.virtualenvs\sample\Scripts\python.exe "C:/Program Files/JetBrains/PyCharm Community Edition 2023.2.3/plugins/python-ce/helpers/pydev/pydevd.py" --multiprocess --qt-support=auto --client 127.0.0.1 --port 58455 --file C:\Users\ADMIN\PycharmProjects\pythonProject1\sample\Person.py 
Connected to pydev debugger (build 232.10072.31)
my name is tom
my name is Jerry
my name is Jerry

Process finished with exit code 0
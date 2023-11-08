class Student:
    school="SVS"
    def __init__(self,m1,m2,m3):#constructors
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def average(self):#instance method
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getschool(cls):#class method
        return cls.school

    @staticmethod
    def info():#static method
        print("static variables ")


s1=Student(31,42,60)
s2=Student(40,50,35)
print(s1.average())
print(Student.getschool())#class method calling-->class name.methodname
Student.info()#static name==clasname.methodname


output:
C:\Users\ADMIN\.virtualenvs\sample\Scripts\python.exe C:\Users\ADMIN\PycharmProjects\pythonProject1\sample\methods.py 
44.333333333333336
SVS
static variables
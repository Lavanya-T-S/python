class A:

    def __init__(self):
        print("inital")

    def feature1(self):
        print("1")
    def feature2(self):
        print("2")
class B(A):
    def __init__(self):
        super().__init__()#super class is used to call constructor
        print("second")
    def lav(self):
        print("hi")

    def kusu(self):#method creation for accessing super class
        super().feature2()#calling method that is lav

obj=B()
obj.feature2()#call method

output
C:\Users\ADMIN\.virtualenvs\sample\Scripts\python.exe C:\Users\ADMIN\PycharmProjects\pythonProject1\sample\constructorinherit.py 
inital
second
2

Process finished with exit code 0
class A:
    def __init__(self):
        print("1st")

    def A1(self):
        print("hi")

class B:
    def __init__(self):
        print("2nd")

    def B1(self):
        print("hello")

class C(A,B):#multiple inheritance
    def __init__(self):
        super().__init__()
        print("3rd")

a1=C()
a1.B1()

output:
C:\Users\ADMIN\.virtualenvs\sample\Scripts\python.exe "C:\Users\ADMIN\PycharmProjects\pythonProject1\sample\method resolution orde.py" 
1st
3rd
hello
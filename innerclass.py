class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno



    def show(self):
        print(self.name,self.rollno)



    class Laptop:
        def __init__(self):
            self.brand=brand
            self.cpu=cpu
            self.ram=ram

        def show(self):
            print(self.brand ,self.cpu,self.ram)



s1=Student("jas",22)
s2=Student("la",24)
s1.show()
l1=Student.Laptop('Hp','i5',8)#object of inner class is created at outside of outer class
l1.show()


class Car:

    wheel=4 #Class or static variable
    def __init__(self):
        self.miles=10
        self.company="BMW"

c1=Car()#object creation
c1.miles=8
c2=Car()#object 

Car.wheel=6#instance variable . 
print(c1.miles,c1.company,c1.wheel)
print(c2.miles,c2.company,c2.wheel)

output:

8 BMW 6
10 BMW 6

Process finished with exit code 0
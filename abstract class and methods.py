from abc import ABC,abstractmethod
class AbstractDemo(ABC):
    @abstractmethod
    def display(self):
        None
    @abstractmethod
    def show(self):
        None
class Demo(AbstractDemo):
    def display(self):
        print("hi0")
class Demo1(AbstractDemo):
    def show(self):
        print("show method")
    def display(self):
        print("hello")
obj=Demo1()
obj.show()
obj.display()
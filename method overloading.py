class Student:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None or c!=None:
            s=a+b
        else:
            s=a
        return s

s1=Student()
print(s1.sum(5,9))

ouutput:
14
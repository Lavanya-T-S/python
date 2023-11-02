class OddNumbers:
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.n=1
        return self
    def __next__(self):
        if self.n>self.max:
            raise StopIteration
        else:
            ForLoopValue=self.n
            self.n+=2
            return ForLoopValue
l=OddNumbers(10)
l=iter(l)
while(True):
    try:
        n=next(l)
        print(n)
    except StopIteration:
        print('got last and now empty')
        break
output:

1
3
5
7
9
got last and now empty
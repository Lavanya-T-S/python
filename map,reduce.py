#map(function,iterable),map performs matematical operation,after filter
def double(n):
    return n*2

nums=[1,2,3,4,5,6,8,9,0]
even=list(filter(lambda n:n%2==0,nums))
print(even)
double =list(map(double,even))
print(double)
#using function
      #or

nums=[2,3,4,5,6,7,9,1]
even=list(filter(lambda n : n%2==0,nums))# filter(function,iterables)
print(even)
doubles=list(map(lambda n:n*2,even))
print(doubles)



           reduce

#for reduce we need to import the funcstools
#reduce(function,sequence),we get only 1 value out of chunk of values
#list is not used bcz we need single output  we are performing addition operation by using 2 values like a+b=c,c+d=e

from functools import reduce
def add_all(a,b):
    return a+b
nums=[1,2,3,4,5,6,7,8,9,0]
even=list(filter(lambda n : n%2==0,nums))# filter(function,iterables)
print(even)
doubles=list(map(lambda n:n*2,even))
print(doubles)
sum=reduce(add_all,doubles )
print(sum)

        #or


nums=[1,2,3,4,5,6,7,8,9,0]
even=list(filter(lambda n : n%2==0,nums))# filter(function,iterables)
print(even)
doubles=list(map(lambda n:n*2,even))
print(doubles)
sum=reduce(lambda a,b:a+b,doubles)
print(sum)
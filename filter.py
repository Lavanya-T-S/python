#filter(function,iterable)
#filter removes unwanted data from a chunk of data
def even(n):
    return n%2==0

nums=[1,2,3,4,5,6,7,8,9,0]
even=list(filter(even,nums))
print(even)
#using function
       #or
#using anonymus block
nums=[2,3,4,5,6,7,9,1]
even=list(filter(lambda n : n%2==0,nums))# filter(function,iterables)
print(even)



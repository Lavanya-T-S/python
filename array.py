number=[4,6,9,1]
number.sort()
print(number)

from array import *
arr=array('i',[])
n=int(input("enter the length of array"))
for i in range(n):
    x=int(input('enter the next values'))
    arr.append(x)
print(arr)

k=0
val=int(input('enter value to search'))
for e in arr:
    if e==val:
        print(k)
        break
    k+=1

print(arr.index(val))











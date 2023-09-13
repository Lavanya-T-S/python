
from numpy import *
arr1=array([1,2,4,3,5,9])
arr2=array([3,2,6,4])
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(sort(arr1))
print(concatenate([arr1,arr2]))


#copying array
arr1=array([2,5,3,1,9,6])
arr2=arr1
print(arr2)
print(arr1)


#shallow copy==use array.view()

array=array([1,2,3,4,56,9])
array2=array.view()
array[2]=0## value changes from 3 to 0 in both array and array2
print(array)
print(array2)
print(id(array))
print(id(array2))


#deep copy==use array.copy()

temp=array([1,3,5,7,9])
temp2=temp.copy()
temp[2]=6## value changes from 5 to 6 in only temp
print(temp)
print(temp2)
print(id(temp))
print(id(temp2))











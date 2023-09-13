#print two array using forloop
arr1=([4,6,2,5,8])
arr2=([9,3,1,0,7])
arr3=([])
k=0
for i in arr1:
    num3=i+arr2[k]
    arr3.append(num3)
    k+=1
print(arr3)
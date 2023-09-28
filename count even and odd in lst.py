def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst=(22,45,11,43,65,76,89)
even,odd=count(lst)

print(even)
print(odd)
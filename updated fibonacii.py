first=0
second=1
last=0
lst=[]
n=int(input('enter a number'))
count=0
while count<n:
    lst.append(last)
    first=second
    second=last
    last=first+second

    count+= 1
print(lst)



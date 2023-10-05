def fact(user):
    f=1
    for i in range(1, user+1):
        f=f*i#1*1=1,1*2=2,2*3=6,6*4=24,24*5=120,
    return f

user=int(input('enter a number'))
result=fact(user)
print(result)
